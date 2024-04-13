# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class EcgSample(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, recording_time_delta_ms: int=None, amplitude_mv: float=None):  # noqa: E501
        """EcgSample - a model defined in Swagger

        :param recording_time_delta_ms: The recording_time_delta_ms of this EcgSample.  # noqa: E501
        :type recording_time_delta_ms: int
        :param amplitude_mv: The amplitude_mv of this EcgSample.  # noqa: E501
        :type amplitude_mv: float
        """
        self.swagger_types = {
            'recording_time_delta_ms': int,
            'amplitude_mv': float
        }

        self.attribute_map = {
            'recording_time_delta_ms': 'recording_time_delta_ms',
            'amplitude_mv': 'amplitude_mv'
        }
        self._recording_time_delta_ms = recording_time_delta_ms
        self._amplitude_mv = amplitude_mv

    @classmethod
    def from_dict(cls, dikt) -> 'EcgSample':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The ecg-sample of this EcgSample.  # noqa: E501
        :rtype: EcgSample
        """
        return util.deserialize_model(dikt, cls)

    @property
    def recording_time_delta_ms(self) -> int:
        """Gets the recording_time_delta_ms of this EcgSample.


        :return: The recording_time_delta_ms of this EcgSample.
        :rtype: int
        """
        return self._recording_time_delta_ms

    @recording_time_delta_ms.setter
    def recording_time_delta_ms(self, recording_time_delta_ms: int):
        """Sets the recording_time_delta_ms of this EcgSample.


        :param recording_time_delta_ms: The recording_time_delta_ms of this EcgSample.
        :type recording_time_delta_ms: int
        """

        self._recording_time_delta_ms = recording_time_delta_ms

    @property
    def amplitude_mv(self) -> float:
        """Gets the amplitude_mv of this EcgSample.


        :return: The amplitude_mv of this EcgSample.
        :rtype: float
        """
        return self._amplitude_mv

    @amplitude_mv.setter
    def amplitude_mv(self, amplitude_mv: float):
        """Sets the amplitude_mv of this EcgSample.


        :param amplitude_mv: The amplitude_mv of this EcgSample.
        :type amplitude_mv: float
        """

        self._amplitude_mv = amplitude_mv
