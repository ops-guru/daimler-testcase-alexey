import logging

import connexion
from flask_testing import LiveServerTestCase, TestCase

from swagger_server import app
from swagger_server.encoder import JSONEncoder
from swagger_server.models.vehicle_push import VehiclePushDataPoint

TRIP_POINT_0_START = VehiclePushDataPoint(
    fuel_level=52,
    odometer=7200,
    position_lat=48.77199,
    position_long=9.172787,
    timestamp=1559137020,
)
TRIP_POINT_1_RUN = VehiclePushDataPoint(
    fuel_level=44,
    odometer=7221,
    position_lat=48.1351,
    position_long=11.5820,
    timestamp=1559137021,
)
TRIP_POINT_2_STOP = VehiclePushDataPoint(
    fuel_level=44,
    odometer=7221,
    position_lat=48.1351,
    position_long=11.5820,
    timestamp=1559137022,
)
TRIP_POINT_3_RUN = VehiclePushDataPoint(
    fuel_level=37,
    odometer=7238,
    position_lat=48.1351,
    position_long=11.5820,
    timestamp=1559137023,
)
TRIP_POINT_4_RUN = VehiclePushDataPoint(
    fuel_level=22,
    odometer=7300,
    position_lat=48.1351,
    position_long=11.5820,
    timestamp=1559137024,
)
TRIP_POINT_5_REFUEL = VehiclePushDataPoint(
    fuel_level=80,
    odometer=7300,
    position_lat=48.1351,
    position_long=11.5820,
    timestamp=1559137025,
)
TRIP_POINT_6_STOP = VehiclePushDataPoint(
    fuel_level=80,
    odometer=7300,
    position_lat=48.1351,
    position_long=11.5820,
    timestamp=1559137026,
)
TRIP_POINT_7_REFUEL = VehiclePushDataPoint(
    fuel_level=95,
    odometer=7300,
    position_lat=48.1351,
    position_long=11.5820,
    timestamp=1559137027,
)
TRIP_POINT_8_RUN = VehiclePushDataPoint(
    fuel_level=80,
    odometer=7310,
    position_lat=48.1351,
    position_long=11.5820,
    timestamp=1559137028,
)
TRIP_POINT_9_STOP = VehiclePushDataPoint(
    fuel_level=80,
    odometer=7310,
    position_lat=48.1351,
    position_long=11.5820,
    timestamp=1559137029,
)
TRIP_POINT_10_FINISH = VehiclePushDataPoint(
    fuel_level=10,
    odometer=7500,
    position_lat=48.1351,
    position_long=11.5820,
    timestamp=1559137030,
)

TRIP_POINTS = [
    TRIP_POINT_0_START,
    TRIP_POINT_1_RUN,
    TRIP_POINT_2_STOP,
    TRIP_POINT_3_RUN,
    TRIP_POINT_4_RUN,
    TRIP_POINT_5_REFUEL,
    TRIP_POINT_6_STOP,
    TRIP_POINT_7_REFUEL,
    TRIP_POINT_8_RUN,
    TRIP_POINT_9_STOP,
    TRIP_POINT_10_FINISH,
]


class BaseLiveTestCase(LiveServerTestCase):
    def create_app(self):
        logging.getLogger("connexion.operation").setLevel("ERROR")
        return app.create_app().app


class BaseTestCase(TestCase):
    def create_app(self):
        logging.getLogger("connexion.operation").setLevel("ERROR")
        return app.create_app().app
