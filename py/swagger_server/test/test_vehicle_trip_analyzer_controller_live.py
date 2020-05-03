# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.vehicle_push import VehiclePush
from swagger_server.models.vehicle_push_analysis import (
    VehiclePushAnalysis,
)
from swagger_server.test import BaseLiveTestCase

from urllib.request import urlopen
import urllib
import urllib.request, urllib.error
import base64


class TestVehicleTripAnalyzerControllerLive(BaseLiveTestCase):
    """VehicleTripAnalyzerController integration test stubs"""

    def test_server_is_up_and_running(self):
        """Test case UI is up and running"""
        response = urlopen(self.get_server_url() + "/v1/ui/")
        self.assertEqual(response.code, 200)

    def test_analyze_noauth(self):
        """Test case no authentication data"""
        body = VehiclePush()
        req = urllib.request.Request(
            self.get_server_url() + "/v1/trip",
            data=json.dumps(body).encode("utf-8"),
            headers={"Content-Type": "application/json"},
        )
        with self.assertRaises(urllib.error.HTTPError) as err:
            response = urlopen(req)

        self.assertEqual(err.exception.code, 401)

    # def test_analyze(self):
    #     """Test case for analyze incorrect data"""
    #     req = urllib.request.Request(
    #         self.get_server_url() + "/v1/trip",
    #         data="HELLO".encode("utf-8"),
    #         headers={"Content-Type": "application/json"},
    #     )
    #     base64string = base64.b64encode(bytes("%s:%s" % ("user", "password"), "ascii"))
    #     req.add_header("Authorization", "Basic %s" % base64string.decode("utf-8"))
    #     response = urlopen(req)
    #     import ptpdb
    #     ptpdb.set_trace()
    #     print(response)


if __name__ == "__main__":
    import unittest

    unittest.main()
