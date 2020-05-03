"""Trip analyzer controller"""

import concurrent.futures
import json
import os
from urllib.request import urlopen

import connexion
from connexion.exceptions import BadRequestProblem, ProblemException

from swagger_server.models.model_break import ModelBreak
from swagger_server.models.model_movement import ModelMovement
from swagger_server.models.vehicle_push import VehiclePush
from swagger_server.models.vehicle_push_analysis import VehiclePushAnalysis

GEO_API_KEY = os.environ.get("GEO_API_KEY", "ec3d0b468c20ef")
URL = "https://locationiq.org/v1/reverse.php?key={}&lat={}&lon={}&format=json"


def find_location(executor, lat: float, long: float):
    def locationiq_get(lat: float, long: float):
        url = URL.format(GEO_API_KEY, lat, long)
        try:
            data = urlopen(url).read()
            location = json.loads(data.decode("utf-8"))
            return location["address"]["city"]
        except Exception as err:
            raise ProblemException(
                status=500,
                title="GEO error for lat:{} long:{}".format(lat, long),
                detail=str(err),
            )

    return executor.submit(locationiq_get, lat, long)


def analyze():
    """analyze a vehicle trip

    this endpoints gets a list of data points from a vehicle. the whole list represents a trip from one location to another with several stops to refuel or just to eat some cookies.

    :param body: vehicle data that needs to be analyzed
    :type body: dict | bytes

    :rtype: VehiclePushAnalysis
    """
    if connexion.request.is_json:
        cities = []
        body = VehiclePush.from_dict(connexion.request.get_json())
        if body.data:
            breaks = []
            refuel_stops = []
            total_distance = 0
            total_consumption = 0
            consumption = 0
            try:
                points = sorted(body.data, key=lambda item: item.timestamp)
                # Transform points to movements
                movements = [
                    ModelMovement(
                        start_timestamp=x.timestamp,
                        end_timestamp=y.timestamp,
                        start_lat=x.position_lat,
                        end_lat=y.position_lat,
                        start_long=x.position_long,
                        end_long=y.position_long,
                        distance=y.odometer - x.odometer,
                        consumption=(
                            (x.fuel_level - y.fuel_level) / 100 * body.gas_tank_size
                        ),
                    )
                    for (x, y) in zip(points[0::1], points[1::1])
                ]
                # Collect data from movements
                for movement in movements:
                    if movement.distance == 0:
                        # There is no movement and timestamp is different
                        breaks.append(
                            ModelBreak(
                                movement.start_timestamp,
                                movement.end_timestamp,
                                movement.start_lat,
                                movement.start_long,
                            )
                        )
                        # There is no movement and timestamp is different, and the level of fuel is increased
                        if movement.consumption < 0:
                            refuel_stops.append(
                                ModelBreak(
                                    movement.start_timestamp,
                                    movement.end_timestamp,
                                    movement.start_lat,
                                    movement.start_long,
                                )
                            )
                    # And I assume that it is impossible to refuel car during movement
                    total_distance += movement.distance
                    if movement.consumption > 0:
                        total_consumption += movement.consumption
                # Find departure and destination
                with concurrent.futures.ThreadPoolExecutor() as executor:
                    city_futures = [
                        find_location(
                            executor, movements[0].start_lat, movements[0].start_long
                        ),
                        find_location(
                            executor, movements[-1].end_lat, movements[-1].end_long
                        ),
                    ]
                    cities = [i.result() for i in city_futures]
                    for city in cities:
                        if isinstance(city, ProblemException):
                            raise city
            except Exception as err:
                raise BadRequestProblem(detail=str(err))
            if total_consumption > 0:
                consumption = total_distance / total_consumption * 100
            return VehiclePushAnalysis(
                vin=body.vin,
                departure=cities[0],
                destination=cities[1],
                refuel_stops=refuel_stops,
                consumption=consumption,
                breaks=breaks,
            )
    raise BadRequestProblem(detail="Request body is not valid JSON")
