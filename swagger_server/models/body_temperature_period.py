# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server.models.body_temperature_sample import BodyTemperatureSample  # noqa: F401,E501
from swagger_server import util


class BodyTemperaturePeriod(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, source_device_id: str=None, measurement_type: str=None, sensor_location: str=None, start_time: datetime=None, end_time: datetime=None, modified_time: datetime=None, samples: List[BodyTemperatureSample]=None):  # noqa: E501
        """BodyTemperaturePeriod - a model defined in Swagger

        :param source_device_id: The source_device_id of this BodyTemperaturePeriod.  # noqa: E501
        :type source_device_id: str
        :param measurement_type: The measurement_type of this BodyTemperaturePeriod.  # noqa: E501
        :type measurement_type: str
        :param sensor_location: The sensor_location of this BodyTemperaturePeriod.  # noqa: E501
        :type sensor_location: str
        :param start_time: The start_time of this BodyTemperaturePeriod.  # noqa: E501
        :type start_time: datetime
        :param end_time: The end_time of this BodyTemperaturePeriod.  # noqa: E501
        :type end_time: datetime
        :param modified_time: The modified_time of this BodyTemperaturePeriod.  # noqa: E501
        :type modified_time: datetime
        :param samples: The samples of this BodyTemperaturePeriod.  # noqa: E501
        :type samples: List[BodyTemperatureSample]
        """
        self.swagger_types = {
            'source_device_id': str,
            'measurement_type': str,
            'sensor_location': str,
            'start_time': datetime,
            'end_time': datetime,
            'modified_time': datetime,
            'samples': List[BodyTemperatureSample]
        }

        self.attribute_map = {
            'source_device_id': 'source_device_id',
            'measurement_type': 'measurement_type',
            'sensor_location': 'sensor_location',
            'start_time': 'start_time',
            'end_time': 'end_time',
            'modified_time': 'modified_time',
            'samples': 'samples'
        }
        self._source_device_id = source_device_id
        self._measurement_type = measurement_type
        self._sensor_location = sensor_location
        self._start_time = start_time
        self._end_time = end_time
        self._modified_time = modified_time
        self._samples = samples

    @classmethod
    def from_dict(cls, dikt) -> 'BodyTemperaturePeriod':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The body-temperature-period of this BodyTemperaturePeriod.  # noqa: E501
        :rtype: BodyTemperaturePeriod
        """
        return util.deserialize_model(dikt, cls)

    @property
    def source_device_id(self) -> str:
        """Gets the source_device_id of this BodyTemperaturePeriod.


        :return: The source_device_id of this BodyTemperaturePeriod.
        :rtype: str
        """
        return self._source_device_id

    @source_device_id.setter
    def source_device_id(self, source_device_id: str):
        """Sets the source_device_id of this BodyTemperaturePeriod.


        :param source_device_id: The source_device_id of this BodyTemperaturePeriod.
        :type source_device_id: str
        """

        self._source_device_id = source_device_id

    @property
    def measurement_type(self) -> str:
        """Gets the measurement_type of this BodyTemperaturePeriod.

        Measurement type  # noqa: E501

        :return: The measurement_type of this BodyTemperaturePeriod.
        :rtype: str
        """
        return self._measurement_type

    @measurement_type.setter
    def measurement_type(self, measurement_type: str):
        """Sets the measurement_type of this BodyTemperaturePeriod.

        Measurement type  # noqa: E501

        :param measurement_type: The measurement_type of this BodyTemperaturePeriod.
        :type measurement_type: str
        """
        allowed_values = ["TM_UNKNOWN", "TM_SKIN_TEMPERATURE", "TM_CORE_TEMPERATURE"]  # noqa: E501
        if measurement_type not in allowed_values:
            raise ValueError(
                "Invalid value for `measurement_type` ({0}), must be one of {1}"
                .format(measurement_type, allowed_values)
            )

        self._measurement_type = measurement_type

    @property
    def sensor_location(self) -> str:
        """Gets the sensor_location of this BodyTemperaturePeriod.

        Sensor location  # noqa: E501

        :return: The sensor_location of this BodyTemperaturePeriod.
        :rtype: str
        """
        return self._sensor_location

    @sensor_location.setter
    def sensor_location(self, sensor_location: str):
        """Sets the sensor_location of this BodyTemperaturePeriod.

        Sensor location  # noqa: E501

        :param sensor_location: The sensor_location of this BodyTemperaturePeriod.
        :type sensor_location: str
        """
        allowed_values = ["SL_UNKNOWN", "SL_DISTAL", "SL_PROXIMAL"]  # noqa: E501
        if sensor_location not in allowed_values:
            raise ValueError(
                "Invalid value for `sensor_location` ({0}), must be one of {1}"
                .format(sensor_location, allowed_values)
            )

        self._sensor_location = sensor_location

    @property
    def start_time(self) -> datetime:
        """Gets the start_time of this BodyTemperaturePeriod.

        Measurement period start time (UTC)  # noqa: E501

        :return: The start_time of this BodyTemperaturePeriod.
        :rtype: datetime
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time: datetime):
        """Sets the start_time of this BodyTemperaturePeriod.

        Measurement period start time (UTC)  # noqa: E501

        :param start_time: The start_time of this BodyTemperaturePeriod.
        :type start_time: datetime
        """

        self._start_time = start_time

    @property
    def end_time(self) -> datetime:
        """Gets the end_time of this BodyTemperaturePeriod.

        Measurement period end time (UTC)  # noqa: E501

        :return: The end_time of this BodyTemperaturePeriod.
        :rtype: datetime
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time: datetime):
        """Sets the end_time of this BodyTemperaturePeriod.

        Measurement period end time (UTC)  # noqa: E501

        :param end_time: The end_time of this BodyTemperaturePeriod.
        :type end_time: datetime
        """

        self._end_time = end_time

    @property
    def modified_time(self) -> datetime:
        """Gets the modified_time of this BodyTemperaturePeriod.

        Measurement period modified time (UTC)  # noqa: E501

        :return: The modified_time of this BodyTemperaturePeriod.
        :rtype: datetime
        """
        return self._modified_time

    @modified_time.setter
    def modified_time(self, modified_time: datetime):
        """Sets the modified_time of this BodyTemperaturePeriod.

        Measurement period modified time (UTC)  # noqa: E501

        :param modified_time: The modified_time of this BodyTemperaturePeriod.
        :type modified_time: datetime
        """

        self._modified_time = modified_time

    @property
    def samples(self) -> List[BodyTemperatureSample]:
        """Gets the samples of this BodyTemperaturePeriod.


        :return: The samples of this BodyTemperaturePeriod.
        :rtype: List[BodyTemperatureSample]
        """
        return self._samples

    @samples.setter
    def samples(self, samples: List[BodyTemperatureSample]):
        """Sets the samples of this BodyTemperaturePeriod.


        :param samples: The samples of this BodyTemperaturePeriod.
        :type samples: List[BodyTemperatureSample]
        """

        self._samples = samples
