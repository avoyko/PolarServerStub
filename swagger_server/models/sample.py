# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class Sample(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, recording_rate: int=None, sample_type: bytearray=None, data: str=None):  # noqa: E501
        """Sample - a model defined in Swagger

        :param recording_rate: The recording_rate of this Sample.  # noqa: E501
        :type recording_rate: int
        :param sample_type: The sample_type of this Sample.  # noqa: E501
        :type sample_type: bytearray
        :param data: The data of this Sample.  # noqa: E501
        :type data: str
        """
        self.swagger_types = {
            'recording_rate': int,
            'sample_type': bytearray,
            'data': str
        }

        self.attribute_map = {
            'recording_rate': 'recording-rate',
            'sample_type': 'sample-type',
            'data': 'data'
        }
        self._recording_rate = recording_rate
        self._sample_type = sample_type
        self._data = data

    @classmethod
    def from_dict(cls, dikt) -> 'Sample':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The sample of this Sample.  # noqa: E501
        :rtype: Sample
        """
        return util.deserialize_model(dikt, cls)

    @property
    def recording_rate(self) -> int:
        """Gets the recording_rate of this Sample.

        Sample recording rate in seconds. Null when recording rate is not applicable - currently only with RR-data.  # noqa: E501

        :return: The recording_rate of this Sample.
        :rtype: int
        """
        return self._recording_rate

    @recording_rate.setter
    def recording_rate(self, recording_rate: int):
        """Sets the recording_rate of this Sample.

        Sample recording rate in seconds. Null when recording rate is not applicable - currently only with RR-data.  # noqa: E501

        :param recording_rate: The recording_rate of this Sample.
        :type recording_rate: int
        """

        self._recording_rate = recording_rate

    @property
    def sample_type(self) -> bytearray:
        """Gets the sample_type of this Sample.

        Sample type  # noqa: E501

        :return: The sample_type of this Sample.
        :rtype: bytearray
        """
        return self._sample_type

    @sample_type.setter
    def sample_type(self, sample_type: bytearray):
        """Sets the sample_type of this Sample.

        Sample type  # noqa: E501

        :param sample_type: The sample_type of this Sample.
        :type sample_type: bytearray
        """

        self._sample_type = sample_type

    @property
    def data(self) -> str:
        """Gets the data of this Sample.

        Sample values as a comma-separated list of strings. Can contain null -values which indicate a situation where sensor was offline.  # noqa: E501

        :return: The data of this Sample.
        :rtype: str
        """
        return self._data

    @data.setter
    def data(self, data: str):
        """Sets the data of this Sample.

        Sample values as a comma-separated list of strings. Can contain null -values which indicate a situation where sensor was offline.  # noqa: E501

        :param data: The data of this Sample.
        :type data: str
        """

        self._data = data
