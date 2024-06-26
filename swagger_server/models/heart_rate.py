# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class HeartRate(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, average: int=None, maximum: int=None):  # noqa: E501
        """HeartRate - a model defined in Swagger

        :param average: The average of this HeartRate.  # noqa: E501
        :type average: int
        :param maximum: The maximum of this HeartRate.  # noqa: E501
        :type maximum: int
        """
        self.swagger_types = {
            'average': int,
            'maximum': int
        }

        self.attribute_map = {
            'average': 'average',
            'maximum': 'maximum'
        }
        self._average = average
        self._maximum = maximum

    @classmethod
    def from_dict(cls, dikt) -> 'HeartRate':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The HeartRate of this HeartRate.  # noqa: E501
        :rtype: HeartRate
        """
        return util.deserialize_model(dikt, cls)

    @property
    def average(self) -> int:
        """Gets the average of this HeartRate.

        Average heart-rate  # noqa: E501

        :return: The average of this HeartRate.
        :rtype: int
        """
        return self._average

    @average.setter
    def average(self, average: int):
        """Sets the average of this HeartRate.

        Average heart-rate  # noqa: E501

        :param average: The average of this HeartRate.
        :type average: int
        """

        self._average = average

    @property
    def maximum(self) -> int:
        """Gets the maximum of this HeartRate.

        Maximum heart-rate  # noqa: E501

        :return: The maximum of this HeartRate.
        :rtype: int
        """
        return self._maximum

    @maximum.setter
    def maximum(self, maximum: int):
        """Sets the maximum of this HeartRate.

        Maximum heart-rate  # noqa: E501

        :param maximum: The maximum of this HeartRate.
        :type maximum: int
        """

        self._maximum = maximum
