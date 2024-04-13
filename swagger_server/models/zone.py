# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class Zone(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, index: int=None, lower_limit: int=None, upper_limit: int=None, in_zone: str=None):  # noqa: E501
        """Zone - a model defined in Swagger

        :param index: The index of this Zone.  # noqa: E501
        :type index: int
        :param lower_limit: The lower_limit of this Zone.  # noqa: E501
        :type lower_limit: int
        :param upper_limit: The upper_limit of this Zone.  # noqa: E501
        :type upper_limit: int
        :param in_zone: The in_zone of this Zone.  # noqa: E501
        :type in_zone: str
        """
        self.swagger_types = {
            'index': int,
            'lower_limit': int,
            'upper_limit': int,
            'in_zone': str
        }

        self.attribute_map = {
            'index': 'index',
            'lower_limit': 'lower-limit',
            'upper_limit': 'upper-limit',
            'in_zone': 'in-zone'
        }
        self._index = index
        self._lower_limit = lower_limit
        self._upper_limit = upper_limit
        self._in_zone = in_zone

    @classmethod
    def from_dict(cls, dikt) -> 'Zone':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The zone of this Zone.  # noqa: E501
        :rtype: Zone
        """
        return util.deserialize_model(dikt, cls)

    @property
    def index(self) -> int:
        """Gets the index of this Zone.

        Zone list index  # noqa: E501

        :return: The index of this Zone.
        :rtype: int
        """
        return self._index

    @index.setter
    def index(self, index: int):
        """Sets the index of this Zone.

        Zone list index  # noqa: E501

        :param index: The index of this Zone.
        :type index: int
        """

        self._index = index

    @property
    def lower_limit(self) -> int:
        """Gets the lower_limit of this Zone.

        Lower heart-rate boundary of the zone  # noqa: E501

        :return: The lower_limit of this Zone.
        :rtype: int
        """
        return self._lower_limit

    @lower_limit.setter
    def lower_limit(self, lower_limit: int):
        """Sets the lower_limit of this Zone.

        Lower heart-rate boundary of the zone  # noqa: E501

        :param lower_limit: The lower_limit of this Zone.
        :type lower_limit: int
        """

        self._lower_limit = lower_limit

    @property
    def upper_limit(self) -> int:
        """Gets the upper_limit of this Zone.

        Upper heart-rate boundary of the zone  # noqa: E501

        :return: The upper_limit of this Zone.
        :rtype: int
        """
        return self._upper_limit

    @upper_limit.setter
    def upper_limit(self, upper_limit: int):
        """Sets the upper_limit of this Zone.

        Upper heart-rate boundary of the zone  # noqa: E501

        :param upper_limit: The upper_limit of this Zone.
        :type upper_limit: int
        """

        self._upper_limit = upper_limit

    @property
    def in_zone(self) -> str:
        """Gets the in_zone of this Zone.

        Time duration spent in the zone ISO 8601  # noqa: E501

        :return: The in_zone of this Zone.
        :rtype: str
        """
        return self._in_zone

    @in_zone.setter
    def in_zone(self, in_zone: str):
        """Sets the in_zone of this Zone.

        Time duration spent in the zone ISO 8601  # noqa: E501

        :param in_zone: The in_zone of this Zone.
        :type in_zone: str
        """

        self._in_zone = in_zone
