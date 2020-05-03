# coding: utf-8

from __future__ import absolute_import

from swagger_server import util
from swagger_server.models.base_model_ import Model


class ModelMovement(Model):
    def __init__(
        self,
        start_timestamp: int,
        end_timestamp: int,
        start_lat: float,
        end_lat: float,
        start_long: float,
        end_long: float,
        distance: int,
        consumption: float,
    ):
        """ModelMovement - a model of movement between two points"""
        self.swagger_types = {
            "start_timestamp": int,
            "end_timestamp": int,
            "start_lat": float,
            "end_lat": float,
            "start_long": float,
            "end_long": float,
            "distance": int,
            "consumption": float,
        }

        self.attribute_map = {
            "start_timestamp": "startTimestamp",
            "end_timestamp": "endTimestamp",
            "start_lat": "startLat",
            "end_lat": "endLat",
            "start_long": "startLong",
            "end_long": "endLong",
            "distance": "distance",
            "consumption": "consumption",
        }

        self._start_timestamp = start_timestamp
        self._end_timestamp = end_timestamp
        self._start_lat = start_lat
        self._end_lat = end_lat
        self._start_long = start_long
        self._end_long = end_long
        self._distance = distance
        self._consumption = consumption

    @classmethod
    def from_dict(cls, dikt) -> "ModelMovement":
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The Movement of this ModelMovement.
        :rtype: ModelMovement
        """
        return util.deserialize_model(dikt, cls)

    @property
    def start_timestamp(self) -> int:
        """Gets the start_timestamp of this ModelMovement."""
        return self._start_timestamp

    @start_timestamp.setter
    def start_timestamp(self, start_timestamp: int):
        """Sets the start_timestamp of this ModelMovement."""
        self._start_timestamp = start_timestamp

    @property
    def end_timestamp(self) -> int:
        """Gets the end_timestamp of this ModelMovement."""
        return self._end_timestamp

    @end_timestamp.setter
    def end_timestamp(self, end_timestamp: int):
        """Sets the end_timestamp of this ModelMovement."""
        self._end_timestamp = end_timestamp

    @property
    def start_lat(self) -> float:
        """Gets the start_lat of this ModelMovement."""
        return self._start_lat

    @start_lat.setter
    def start_lat(self, start_lat: float):
        """Sets the start_lat of this ModelMovement."""
        self._start_lat = start_lat

    @property
    def end_lat(self) -> float:
        """Gets the end_lat of this ModelMovement."""
        return self._end_lat

    @end_lat.setter
    def end_lat(self, end_lat: float):
        """Sets the end_lat of this ModelMovement."""
        self._end_lat = end_lat

    @property
    def start_long(self) -> float:
        """Gets the start_long of this ModelMovement."""
        return self._start_long

    @start_long.setter
    def start_long(self, start_long: float):
        """Sets the start_long of this ModelMovement."""
        self._start_long = start_long

    @property
    def end_long(self) -> float:
        """Gets the end_long of this ModelMovement."""
        return self._end_long

    @end_long.setter
    def end_long(self, end_long: float):
        """Sets the end_long of this ModelMovement."""
        self._end_long = end_long

    @property
    def distance(self) -> int:
        """Gets the distance of this ModelMovement."""
        return self._distance

    @distance.setter
    def distance(self, distance: int):
        """Sets the distance of this ModelMovement."""
        self._distance = distance

    @property
    def consumption(self) -> int:
        """Gets the consumption of this ModelMovement."""
        return self._consumption

    @consumption.setter
    def consumption(self, consumption: int):
        """Sets the consumption of this ModelMovement."""
        self._consumption = consumption
