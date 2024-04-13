# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server.models.duration_zone import DurationZone  # noqa: F401,E501
from swagger_server import util


class ActivityZoneSample(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, activity_zones: List[DurationZone]=None, time: str=None):  # noqa: E501
        """ActivityZoneSample - a model defined in Swagger

        :param activity_zones: The activity_zones of this ActivityZoneSample.  # noqa: E501
        :type activity_zones: List[DurationZone]
        :param time: The time of this ActivityZoneSample.  # noqa: E501
        :type time: str
        """
        self.swagger_types = {
            'activity_zones': List[DurationZone],
            'time': str
        }

        self.attribute_map = {
            'activity_zones': 'activity-zones',
            'time': 'time'
        }
        self._activity_zones = activity_zones
        self._time = time

    @classmethod
    def from_dict(cls, dikt) -> 'ActivityZoneSample':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The activity-zone-sample of this ActivityZoneSample.  # noqa: E501
        :rtype: ActivityZoneSample
        """
        return util.deserialize_model(dikt, cls)

    @property
    def activity_zones(self) -> List[DurationZone]:
        """Gets the activity_zones of this ActivityZoneSample.

        List of heart rate zones with duration.  # noqa: E501

        :return: The activity_zones of this ActivityZoneSample.
        :rtype: List[DurationZone]
        """
        return self._activity_zones

    @activity_zones.setter
    def activity_zones(self, activity_zones: List[DurationZone]):
        """Sets the activity_zones of this ActivityZoneSample.

        List of heart rate zones with duration.  # noqa: E501

        :param activity_zones: The activity_zones of this ActivityZoneSample.
        :type activity_zones: List[DurationZone]
        """

        self._activity_zones = activity_zones

    @property
    def time(self) -> str:
        """Gets the time of this ActivityZoneSample.

        Start time of sample segment.  # noqa: E501

        :return: The time of this ActivityZoneSample.
        :rtype: str
        """
        return self._time

    @time.setter
    def time(self, time: str):
        """Sets the time of this ActivityZoneSample.

        Start time of sample segment.  # noqa: E501

        :param time: The time of this ActivityZoneSample.
        :type time: str
        """

        self._time = time
