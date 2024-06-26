# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class Location(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, latitude: float=None, longitude: float=None, time: str=None, satellites: int=None, fix: int=None):  # noqa: E501
        """Location - a model defined in Swagger

        :param latitude: The latitude of this Location.  # noqa: E501
        :type latitude: float
        :param longitude: The longitude of this Location.  # noqa: E501
        :type longitude: float
        :param time: The time of this Location.  # noqa: E501
        :type time: str
        :param satellites: The satellites of this Location.  # noqa: E501
        :type satellites: int
        :param fix: The fix of this Location.  # noqa: E501
        :type fix: int
        """
        self.swagger_types = {
            'latitude': float,
            'longitude': float,
            'time': str,
            'satellites': int,
            'fix': int
        }

        self.attribute_map = {
            'latitude': 'latitude',
            'longitude': 'longitude',
            'time': 'time',
            'satellites': 'satellites',
            'fix': 'fix'
        }
        self._latitude = latitude
        self._longitude = longitude
        self._time = time
        self._satellites = satellites
        self._fix = fix

    @classmethod
    def from_dict(cls, dikt) -> 'Location':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The location of this Location.  # noqa: E501
        :rtype: Location
        """
        return util.deserialize_model(dikt, cls)

    @property
    def latitude(self) -> float:
        """Gets the latitude of this Location.

        The latitude, expressed in degrees.  # noqa: E501

        :return: The latitude of this Location.
        :rtype: float
        """
        return self._latitude

    @latitude.setter
    def latitude(self, latitude: float):
        """Sets the latitude of this Location.

        The latitude, expressed in degrees.  # noqa: E501

        :param latitude: The latitude of this Location.
        :type latitude: float
        """

        self._latitude = latitude

    @property
    def longitude(self) -> float:
        """Gets the longitude of this Location.

        The longitude, expressed in degrees.  # noqa: E501

        :return: The longitude of this Location.
        :rtype: float
        """
        return self._longitude

    @longitude.setter
    def longitude(self, longitude: float):
        """Sets the longitude of this Location.

        The longitude, expressed in degrees.  # noqa: E501

        :param longitude: The longitude of this Location.
        :type longitude: float
        """

        self._longitude = longitude

    @property
    def time(self) -> str:
        """Gets the time of this Location.

        The time, expressed as a duration.  # noqa: E501

        :return: The time of this Location.
        :rtype: str
        """
        return self._time

    @time.setter
    def time(self, time: str):
        """Sets the time of this Location.

        The time, expressed as a duration.  # noqa: E501

        :param time: The time of this Location.
        :type time: str
        """

        self._time = time

    @property
    def satellites(self) -> int:
        """Gets the satellites of this Location.

        Satellites. A byte-sized value with a maximum of 63.  # noqa: E501

        :return: The satellites of this Location.
        :rtype: int
        """
        return self._satellites

    @satellites.setter
    def satellites(self, satellites: int):
        """Sets the satellites of this Location.

        Satellites. A byte-sized value with a maximum of 63.  # noqa: E501

        :param satellites: The satellites of this Location.
        :type satellites: int
        """

        self._satellites = satellites

    @property
    def fix(self) -> int:
        """Gets the fix of this Location.

        Fix. A byte-sized value with a maximum of three.  # noqa: E501

        :return: The fix of this Location.
        :rtype: int
        """
        return self._fix

    @fix.setter
    def fix(self, fix: int):
        """Sets the fix of this Location.

        Fix. A byte-sized value with a maximum of three.  # noqa: E501

        :param fix: The fix of this Location.
        :type fix: int
        """

        self._fix = fix
