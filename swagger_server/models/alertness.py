# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server.models.alertness_hourly_data import AlertnessHourlyData  # noqa: F401,E501
from swagger_server import util


class Alertness(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, grade: float=None, grade_validity_seconds: float=None, grade_type: str=None, grade_classification: str=None, validity: str=None, sleep_inertia: str=None, sleep_type: str=None, result_type: str=None, period_start_time: date=None, period_end_time: date=None, sleep_period_start_time: date=None, sleep_period_end_time: date=None, sleep_timezone_offset_minutes: float=None, hourly_data: List[AlertnessHourlyData]=None):  # noqa: E501
        """Alertness - a model defined in Swagger

        :param grade: The grade of this Alertness.  # noqa: E501
        :type grade: float
        :param grade_validity_seconds: The grade_validity_seconds of this Alertness.  # noqa: E501
        :type grade_validity_seconds: float
        :param grade_type: The grade_type of this Alertness.  # noqa: E501
        :type grade_type: str
        :param grade_classification: The grade_classification of this Alertness.  # noqa: E501
        :type grade_classification: str
        :param validity: The validity of this Alertness.  # noqa: E501
        :type validity: str
        :param sleep_inertia: The sleep_inertia of this Alertness.  # noqa: E501
        :type sleep_inertia: str
        :param sleep_type: The sleep_type of this Alertness.  # noqa: E501
        :type sleep_type: str
        :param result_type: The result_type of this Alertness.  # noqa: E501
        :type result_type: str
        :param period_start_time: The period_start_time of this Alertness.  # noqa: E501
        :type period_start_time: date
        :param period_end_time: The period_end_time of this Alertness.  # noqa: E501
        :type period_end_time: date
        :param sleep_period_start_time: The sleep_period_start_time of this Alertness.  # noqa: E501
        :type sleep_period_start_time: date
        :param sleep_period_end_time: The sleep_period_end_time of this Alertness.  # noqa: E501
        :type sleep_period_end_time: date
        :param sleep_timezone_offset_minutes: The sleep_timezone_offset_minutes of this Alertness.  # noqa: E501
        :type sleep_timezone_offset_minutes: float
        :param hourly_data: The hourly_data of this Alertness.  # noqa: E501
        :type hourly_data: List[AlertnessHourlyData]
        """
        self.swagger_types = {
            'grade': float,
            'grade_validity_seconds': float,
            'grade_type': str,
            'grade_classification': str,
            'validity': str,
            'sleep_inertia': str,
            'sleep_type': str,
            'result_type': str,
            'period_start_time': date,
            'period_end_time': date,
            'sleep_period_start_time': date,
            'sleep_period_end_time': date,
            'sleep_timezone_offset_minutes': float,
            'hourly_data': List[AlertnessHourlyData]
        }

        self.attribute_map = {
            'grade': 'grade',
            'grade_validity_seconds': 'grade_validity_seconds',
            'grade_type': 'grade_type',
            'grade_classification': 'grade_classification',
            'validity': 'validity',
            'sleep_inertia': 'sleep_inertia',
            'sleep_type': 'sleep_type',
            'result_type': 'result_type',
            'period_start_time': 'period_start_time',
            'period_end_time': 'period_end_time',
            'sleep_period_start_time': 'sleep_period_start_time',
            'sleep_period_end_time': 'sleep_period_end_time',
            'sleep_timezone_offset_minutes': 'sleep_timezone_offset_minutes',
            'hourly_data': 'hourly_data'
        }
        self._grade = grade
        self._grade_validity_seconds = grade_validity_seconds
        self._grade_type = grade_type
        self._grade_classification = grade_classification
        self._validity = validity
        self._sleep_inertia = sleep_inertia
        self._sleep_type = sleep_type
        self._result_type = result_type
        self._period_start_time = period_start_time
        self._period_end_time = period_end_time
        self._sleep_period_start_time = sleep_period_start_time
        self._sleep_period_end_time = sleep_period_end_time
        self._sleep_timezone_offset_minutes = sleep_timezone_offset_minutes
        self._hourly_data = hourly_data

    @classmethod
    def from_dict(cls, dikt) -> 'Alertness':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The alertness of this Alertness.  # noqa: E501
        :rtype: Alertness
        """
        return util.deserialize_model(dikt, cls)

    @property
    def grade(self) -> float:
        """Gets the grade of this Alertness.

        Grade  # noqa: E501

        :return: The grade of this Alertness.
        :rtype: float
        """
        return self._grade

    @grade.setter
    def grade(self, grade: float):
        """Sets the grade of this Alertness.

        Grade  # noqa: E501

        :param grade: The grade of this Alertness.
        :type grade: float
        """

        self._grade = grade

    @property
    def grade_validity_seconds(self) -> float:
        """Gets the grade_validity_seconds of this Alertness.

        Grade validity seconds  # noqa: E501

        :return: The grade_validity_seconds of this Alertness.
        :rtype: float
        """
        return self._grade_validity_seconds

    @grade_validity_seconds.setter
    def grade_validity_seconds(self, grade_validity_seconds: float):
        """Sets the grade_validity_seconds of this Alertness.

        Grade validity seconds  # noqa: E501

        :param grade_validity_seconds: The grade_validity_seconds of this Alertness.
        :type grade_validity_seconds: float
        """

        self._grade_validity_seconds = grade_validity_seconds

    @property
    def grade_type(self) -> str:
        """Gets the grade_type of this Alertness.

        Grade type  # noqa: E501

        :return: The grade_type of this Alertness.
        :rtype: str
        """
        return self._grade_type

    @grade_type.setter
    def grade_type(self, grade_type: str):
        """Sets the grade_type of this Alertness.

        Grade type  # noqa: E501

        :param grade_type: The grade_type of this Alertness.
        :type grade_type: str
        """
        allowed_values = ["GRADE_TYPE_UNKNOWN", "GRADE_TYPE_PRIMARY", "GRADE_TYPE_ADDITIONAL"]  # noqa: E501
        if grade_type not in allowed_values:
            raise ValueError(
                "Invalid value for `grade_type` ({0}), must be one of {1}"
                .format(grade_type, allowed_values)
            )

        self._grade_type = grade_type

    @property
    def grade_classification(self) -> str:
        """Gets the grade_classification of this Alertness.

        Grade classification  # noqa: E501

        :return: The grade_classification of this Alertness.
        :rtype: str
        """
        return self._grade_classification

    @grade_classification.setter
    def grade_classification(self, grade_classification: str):
        """Sets the grade_classification of this Alertness.

        Grade classification  # noqa: E501

        :param grade_classification: The grade_classification of this Alertness.
        :type grade_classification: str
        """
        allowed_values = ["GRADE_CLASSIFICATION_UNKNOWN", "GRADE_CLASSIFICATION_WEAK", "GRADE_CLASSIFICATION_FAIR", "GRADE_CLASSIFICATION_STRONG", "GRADE_CLASSIFICATION_EXCELLENT"]  # noqa: E501
        if grade_classification not in allowed_values:
            raise ValueError(
                "Invalid value for `grade_classification` ({0}), must be one of {1}"
                .format(grade_classification, allowed_values)
            )

        self._grade_classification = grade_classification

    @property
    def validity(self) -> str:
        """Gets the validity of this Alertness.

        Validity  # noqa: E501

        :return: The validity of this Alertness.
        :rtype: str
        """
        return self._validity

    @validity.setter
    def validity(self, validity: str):
        """Sets the validity of this Alertness.

        Validity  # noqa: E501

        :param validity: The validity of this Alertness.
        :type validity: str
        """
        allowed_values = ["VALIDITY_UNKNOWN", "VALIDITY_RESET", "VALIDITY_NOT_VALID", "VALIDITY_ESTIMATE", "VALIDITY_VALID"]  # noqa: E501
        if validity not in allowed_values:
            raise ValueError(
                "Invalid value for `validity` ({0}), must be one of {1}"
                .format(validity, allowed_values)
            )

        self._validity = validity

    @property
    def sleep_inertia(self) -> str:
        """Gets the sleep_inertia of this Alertness.

        Sleep inertia  # noqa: E501

        :return: The sleep_inertia of this Alertness.
        :rtype: str
        """
        return self._sleep_inertia

    @sleep_inertia.setter
    def sleep_inertia(self, sleep_inertia: str):
        """Sets the sleep_inertia of this Alertness.

        Sleep inertia  # noqa: E501

        :param sleep_inertia: The sleep_inertia of this Alertness.
        :type sleep_inertia: str
        """
        allowed_values = ["SLEEP_INERTIA_UNKNOWN", "SLEEP_INERTIA_NO_INERTIA", "SLEEP_INERTIA_MILD", "SLEEP_INERTIA_MODERATE", "SLEEP_INERTIA_HEAVY"]  # noqa: E501
        if sleep_inertia not in allowed_values:
            raise ValueError(
                "Invalid value for `sleep_inertia` ({0}), must be one of {1}"
                .format(sleep_inertia, allowed_values)
            )

        self._sleep_inertia = sleep_inertia

    @property
    def sleep_type(self) -> str:
        """Gets the sleep_type of this Alertness.

        Sleep type  # noqa: E501

        :return: The sleep_type of this Alertness.
        :rtype: str
        """
        return self._sleep_type

    @sleep_type.setter
    def sleep_type(self, sleep_type: str):
        """Sets the sleep_type of this Alertness.

        Sleep type  # noqa: E501

        :param sleep_type: The sleep_type of this Alertness.
        :type sleep_type: str
        """
        allowed_values = ["SLEEP_TYPE_UNKNOWN", "SLEEP_TYPE_PRIMARY", "SLEEP_TYPE_SECONDARY", "SLEEP_TYPE_ARTIFICIAL"]  # noqa: E501
        if sleep_type not in allowed_values:
            raise ValueError(
                "Invalid value for `sleep_type` ({0}), must be one of {1}"
                .format(sleep_type, allowed_values)
            )

        self._sleep_type = sleep_type

    @property
    def result_type(self) -> str:
        """Gets the result_type of this Alertness.

        Result type  # noqa: E501

        :return: The result_type of this Alertness.
        :rtype: str
        """
        return self._result_type

    @result_type.setter
    def result_type(self, result_type: str):
        """Sets the result_type of this Alertness.

        Result type  # noqa: E501

        :param result_type: The result_type of this Alertness.
        :type result_type: str
        """
        allowed_values = ["ALERTNESS_TYPE_UNKNOWN", "ALERTNESS_TYPE_PREDICTION", "ALERTNESS_TYPE_HISTORY"]  # noqa: E501
        if result_type not in allowed_values:
            raise ValueError(
                "Invalid value for `result_type` ({0}), must be one of {1}"
                .format(result_type, allowed_values)
            )

        self._result_type = result_type

    @property
    def period_start_time(self) -> date:
        """Gets the period_start_time of this Alertness.

        Alertness period start time (UTC)  # noqa: E501

        :return: The period_start_time of this Alertness.
        :rtype: date
        """
        return self._period_start_time

    @period_start_time.setter
    def period_start_time(self, period_start_time: date):
        """Sets the period_start_time of this Alertness.

        Alertness period start time (UTC)  # noqa: E501

        :param period_start_time: The period_start_time of this Alertness.
        :type period_start_time: date
        """

        self._period_start_time = period_start_time

    @property
    def period_end_time(self) -> date:
        """Gets the period_end_time of this Alertness.

        Alertness period end time (UTC)  # noqa: E501

        :return: The period_end_time of this Alertness.
        :rtype: date
        """
        return self._period_end_time

    @period_end_time.setter
    def period_end_time(self, period_end_time: date):
        """Sets the period_end_time of this Alertness.

        Alertness period end time (UTC)  # noqa: E501

        :param period_end_time: The period_end_time of this Alertness.
        :type period_end_time: date
        """

        self._period_end_time = period_end_time

    @property
    def sleep_period_start_time(self) -> date:
        """Gets the sleep_period_start_time of this Alertness.

        Sleep period start time (UTC)  # noqa: E501

        :return: The sleep_period_start_time of this Alertness.
        :rtype: date
        """
        return self._sleep_period_start_time

    @sleep_period_start_time.setter
    def sleep_period_start_time(self, sleep_period_start_time: date):
        """Sets the sleep_period_start_time of this Alertness.

        Sleep period start time (UTC)  # noqa: E501

        :param sleep_period_start_time: The sleep_period_start_time of this Alertness.
        :type sleep_period_start_time: date
        """

        self._sleep_period_start_time = sleep_period_start_time

    @property
    def sleep_period_end_time(self) -> date:
        """Gets the sleep_period_end_time of this Alertness.

        Sleep period end time (UTC)  # noqa: E501

        :return: The sleep_period_end_time of this Alertness.
        :rtype: date
        """
        return self._sleep_period_end_time

    @sleep_period_end_time.setter
    def sleep_period_end_time(self, sleep_period_end_time: date):
        """Sets the sleep_period_end_time of this Alertness.

        Sleep period end time (UTC)  # noqa: E501

        :param sleep_period_end_time: The sleep_period_end_time of this Alertness.
        :type sleep_period_end_time: date
        """

        self._sleep_period_end_time = sleep_period_end_time

    @property
    def sleep_timezone_offset_minutes(self) -> float:
        """Gets the sleep_timezone_offset_minutes of this Alertness.

        Sleep timezone offset minutes  # noqa: E501

        :return: The sleep_timezone_offset_minutes of this Alertness.
        :rtype: float
        """
        return self._sleep_timezone_offset_minutes

    @sleep_timezone_offset_minutes.setter
    def sleep_timezone_offset_minutes(self, sleep_timezone_offset_minutes: float):
        """Sets the sleep_timezone_offset_minutes of this Alertness.

        Sleep timezone offset minutes  # noqa: E501

        :param sleep_timezone_offset_minutes: The sleep_timezone_offset_minutes of this Alertness.
        :type sleep_timezone_offset_minutes: float
        """

        self._sleep_timezone_offset_minutes = sleep_timezone_offset_minutes

    @property
    def hourly_data(self) -> List[AlertnessHourlyData]:
        """Gets the hourly_data of this Alertness.

        Alertness hourly data for the alertness period  # noqa: E501

        :return: The hourly_data of this Alertness.
        :rtype: List[AlertnessHourlyData]
        """
        return self._hourly_data

    @hourly_data.setter
    def hourly_data(self, hourly_data: List[AlertnessHourlyData]):
        """Sets the hourly_data of this Alertness.

        Alertness hourly data for the alertness period  # noqa: E501

        :param hourly_data: The hourly_data of this Alertness.
        :type hourly_data: List[AlertnessHourlyData]
        """

        self._hourly_data = hourly_data
