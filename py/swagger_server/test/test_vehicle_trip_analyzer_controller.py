# coding: utf-8
"""Test service with Flask Test Client"""

from __future__ import absolute_import

import base64
import random

from flask import json

from swagger_server.models.vehicle_push import VehiclePush, VehiclePushDataPoint
from swagger_server.test import (
    TRIP_POINTS,
    BaseTestCase,
    TRIP_POINT_4_RUN,
    TRIP_POINT_6_STOP,
)


class TestVehicleTripAnalyzerController(BaseTestCase):
    """VehicleTripAnalyzerController integration test stubs"""

    def test_server_is_up_and_running(self):
        """Test case UI is up and running"""
        response = self.client.open("/v1/ui/")
        self.assert200(response, "Response body is : " + response.data.decode("utf-8"))

    def test_analyze_noauth(self):
        """Test case no auth"""
        body = VehiclePush()
        response = self.client.open(
            "/v1/trip",
            method="POST",
            data=json.dumps(body),
            content_type="application/json",
        )
        self.assert401(response, "Response body is : " + response.data.decode("utf-8"))

    def test_405_get(self):
        """Test case for 405 GET"""
        base64string = base64.b64encode(bytes("%s:%s" % ("user", "password"), "ascii"))
        headers = {
            "Accept": "application/json",
            "Content-Type": "application/json",
            "Authorization": "Basic %s" % base64string.decode("utf-8"),
        }
        response = self.client.open("/v1/trip", method="GET", headers=headers)
        self.assert405(response, "Response body is : " + response.data.decode("utf-8"))
        self.assertEqual(response.headers["Allow"], "POST")

    def test_field_validator_break_threshold(self):
        """Test field validator breakThreshold"""
        body = {"breakThreshold": "abc", "gasTankSize": 80, "vin": "WDD1671591Z000999"}
        base64string = base64.b64encode(bytes("%s:%s" % ("user", "password"), "ascii"))
        headers = {
            "Accept": "application/json",
            "Content-Type": "application/json",
            "Authorization": "Basic %s" % base64string.decode("utf-8"),
        }
        response = self.client.open(
            "/v1/trip",
            method="POST",
            data=json.dumps(body).encode("utf-8"),
            headers=headers,
        )
        self.assert400(response, "Response body is : " + response.data.decode("utf-8"))

    def test_field_validator_fuel_min(self):
        """Test field validator fuel MIN"""
        body = {
            "breakThreshold": 1800,
            "gasTankSize": 80,
            "vin": "WDD1671591Z000999",
            "data": [
                {
                    "fuelLevel": -1,
                    "odometer": 7200,
                    "positionLat": 48.77199,
                    "positionLong": 9.172787,
                }
            ],
        }
        base64string = base64.b64encode(bytes("%s:%s" % ("user", "password"), "ascii"))
        headers = {
            "Accept": "application/json",
            "Content-Type": "application/json",
            "Authorization": "Basic %s" % base64string.decode("utf-8"),
        }
        response = self.client.open(
            "/v1/trip",
            method="POST",
            data=json.dumps(body).encode("utf-8"),
            headers=headers,
        )
        self.assert400(response, "Response body is : " + response.data.decode("utf-8"))

    def test_field_validator_fuel_max(self):
        """Test field validator fuel MAX"""
        body = {
            "breakThreshold": 1800,
            "gasTankSize": 80,
            "vin": "WDD1671591Z000999",
            "data": [
                {
                    "fuelLevel": 101,
                    "odometer": 7200,
                    "positionLat": 48.77199,
                    "positionLong": 9.172787,
                }
            ],
        }
        base64string = base64.b64encode(bytes("%s:%s" % ("user", "password"), "ascii"))
        headers = {
            "Accept": "application/json",
            "Content-Type": "application/json",
            "Authorization": "Basic %s" % base64string.decode("utf-8"),
        }
        response = self.client.open(
            "/v1/trip",
            method="POST",
            data=json.dumps(body).encode("utf-8"),
            headers=headers,
        )
        self.assert400(response, "Response body is : " + response.data.decode("utf-8"))

    def test_field_validator_position_lat(self):
        """Test field validator positionLat"""
        body = {
            "breakThreshold": 1800,
            "gasTankSize": 80,
            "vin": "WDD1671591Z000999",
            "data": [
                {
                    "fuelLevel": 52,
                    "odometer": 7200,
                    "positionLat": "xyz",
                    "positionLong": 9.172787,
                }
            ],
        }
        base64string = base64.b64encode(bytes("%s:%s" % ("user", "password"), "ascii"))
        headers = {
            "Accept": "application/json",
            "Content-Type": "application/json",
            "Authorization": "Basic %s" % base64string.decode("utf-8"),
        }
        response = self.client.open(
            "/v1/trip",
            method="POST",
            data=json.dumps(body).encode("utf-8"),
            headers=headers,
        )
        self.assert400(response, "Response body is : " + response.data.decode("utf-8"))

    def test_input_analysis(self):
        """Test input analysis"""
        trip = TRIP_POINTS.copy()
        random.shuffle(trip)
        body = VehiclePush(
            vin="WDD1671591Z000999", break_threshold=1800, gas_tank_size=80, data=trip,
        )
        base64string = base64.b64encode(bytes("%s:%s" % ("user", "password"), "ascii"))
        headers = {
            "Accept": "application/json",
            "Content-Type": "application/json",
            "Authorization": "Basic %s" % base64string.decode("utf-8"),
        }
        response = self.client.open(
            "/v1/trip",
            method="POST",
            data=json.dumps(body).encode("utf-8"),
            headers=headers,
        )
        self.assert200(response, "Response body is : " + response.data.decode("utf-8"))
        result = json.loads(response.data.decode("utf-8"))
        self.assertEqual(result["departure"], "Stuttgart")
        self.assertEqual(result["destination"], "Munich")
        # We refueled car after points 4 and 6
        self.assertListEqual(
            sorted(i["startTimestamp"] for i in result["refuelStops"]),
            [TRIP_POINT_4_RUN.timestamp, TRIP_POINT_6_STOP.timestamp],
        )
        self.assertEqual(len(result["breaks"]), 5)

    def test_generate_trip(self):
        block = """
        - positionLong: {}
          fuelLevel: {}
          odometer: {}
          positionLat: {}
          timestamp: {}
        """
        for i in TRIP_POINTS:
            print(
                block.format(
                    i.position_long,
                    i.fuel_level,
                    i.odometer,
                    i.position_lat,
                    i.timestamp,
                )
            )


if __name__ == "__main__":
    import unittest

    unittest.main()
