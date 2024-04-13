# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server.models.heart_rate import HeartRate  # noqa: F401,E501
from swagger_server.models.training_load_pro_sample import TrainingLoadProSample  # noqa: F401,E501
from swagger_server import util


class Exercise(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, id: int=None, upload_time: str=None, polar_user: str=None, transaction_id: int=None, device: str=None, device_id: str=None, start_time: str=None, start_time_utc_offset: int=None, duration: str=None, calories: int=None, distance: float=None, heart_rate: HeartRate=None, training_load: float=None, sport: str=None, has_route: bool=None, club_id: int=None, club_name: str=None, detailed_sport_info: str=None, fat_percentage: int=None, carbohydrate_percentage: int=None, protein_percentage: int=None, running_index: int=None, training_load_pro: List[TrainingLoadProSample]=None):  # noqa: E501
        """Exercise - a model defined in Swagger

        :param id: The id of this Exercise.  # noqa: E501
        :type id: int
        :param upload_time: The upload_time of this Exercise.  # noqa: E501
        :type upload_time: str
        :param polar_user: The polar_user of this Exercise.  # noqa: E501
        :type polar_user: str
        :param transaction_id: The transaction_id of this Exercise.  # noqa: E501
        :type transaction_id: int
        :param device: The device of this Exercise.  # noqa: E501
        :type device: str
        :param device_id: The device_id of this Exercise.  # noqa: E501
        :type device_id: str
        :param start_time: The start_time of this Exercise.  # noqa: E501
        :type start_time: str
        :param start_time_utc_offset: The start_time_utc_offset of this Exercise.  # noqa: E501
        :type start_time_utc_offset: int
        :param duration: The duration of this Exercise.  # noqa: E501
        :type duration: str
        :param calories: The calories of this Exercise.  # noqa: E501
        :type calories: int
        :param distance: The distance of this Exercise.  # noqa: E501
        :type distance: float
        :param heart_rate: The heart_rate of this Exercise.  # noqa: E501
        :type heart_rate: HeartRate
        :param training_load: The training_load of this Exercise.  # noqa: E501
        :type training_load: float
        :param sport: The sport of this Exercise.  # noqa: E501
        :type sport: str
        :param has_route: The has_route of this Exercise.  # noqa: E501
        :type has_route: bool
        :param club_id: The club_id of this Exercise.  # noqa: E501
        :type club_id: int
        :param club_name: The club_name of this Exercise.  # noqa: E501
        :type club_name: str
        :param detailed_sport_info: The detailed_sport_info of this Exercise.  # noqa: E501
        :type detailed_sport_info: str
        :param fat_percentage: The fat_percentage of this Exercise.  # noqa: E501
        :type fat_percentage: int
        :param carbohydrate_percentage: The carbohydrate_percentage of this Exercise.  # noqa: E501
        :type carbohydrate_percentage: int
        :param protein_percentage: The protein_percentage of this Exercise.  # noqa: E501
        :type protein_percentage: int
        :param running_index: The running_index of this Exercise.  # noqa: E501
        :type running_index: int
        :param training_load_pro: The training_load_pro of this Exercise.  # noqa: E501
        :type training_load_pro: List[TrainingLoadProSample]
        """
        self.swagger_types = {
            'id': int,
            'upload_time': str,
            'polar_user': str,
            'transaction_id': int,
            'device': str,
            'device_id': str,
            'start_time': str,
            'start_time_utc_offset': int,
            'duration': str,
            'calories': int,
            'distance': float,
            'heart_rate': HeartRate,
            'training_load': float,
            'sport': str,
            'has_route': bool,
            'club_id': int,
            'club_name': str,
            'detailed_sport_info': str,
            'fat_percentage': int,
            'carbohydrate_percentage': int,
            'protein_percentage': int,
            'running_index': int,
            'training_load_pro': List[TrainingLoadProSample]
        }

        self.attribute_map = {
            'id': 'id',
            'upload_time': 'upload-time',
            'polar_user': 'polar-user',
            'transaction_id': 'transaction-id',
            'device': 'device',
            'device_id': 'device-id',
            'start_time': 'start-time',
            'start_time_utc_offset': 'start-time-utc-offset',
            'duration': 'duration',
            'calories': 'calories',
            'distance': 'distance',
            'heart_rate': 'heart-rate',
            'training_load': 'training-load',
            'sport': 'sport',
            'has_route': 'has-route',
            'club_id': 'club-id',
            'club_name': 'club-name',
            'detailed_sport_info': 'detailed-sport-info',
            'fat_percentage': 'fat-percentage',
            'carbohydrate_percentage': 'carbohydrate-percentage',
            'protein_percentage': 'protein-percentage',
            'running_index': 'running-index',
            'training_load_pro': 'training-load-pro'
        }
        self._id = id
        self._upload_time = upload_time
        self._polar_user = polar_user
        self._transaction_id = transaction_id
        self._device = device
        self._device_id = device_id
        self._start_time = start_time
        self._start_time_utc_offset = start_time_utc_offset
        self._duration = duration
        self._calories = calories
        self._distance = distance
        self._heart_rate = heart_rate
        self._training_load = training_load
        self._sport = sport
        self._has_route = has_route
        self._club_id = club_id
        self._club_name = club_name
        self._detailed_sport_info = detailed_sport_info
        self._fat_percentage = fat_percentage
        self._carbohydrate_percentage = carbohydrate_percentage
        self._protein_percentage = protein_percentage
        self._running_index = running_index
        self._training_load_pro = training_load_pro

    @classmethod
    def from_dict(cls, dikt) -> 'Exercise':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The exercise of this Exercise.  # noqa: E501
        :rtype: Exercise
        """
        return util.deserialize_model(dikt, cls)

    @property
    def id(self) -> int:
        """Gets the id of this Exercise.

        Id of the trainining session  # noqa: E501

        :return: The id of this Exercise.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id: int):
        """Sets the id of this Exercise.

        Id of the trainining session  # noqa: E501

        :param id: The id of this Exercise.
        :type id: int
        """

        self._id = id

    @property
    def upload_time(self) -> str:
        """Gets the upload_time of this Exercise.

        Time of the transfer from wrist unit to Polar database  # noqa: E501

        :return: The upload_time of this Exercise.
        :rtype: str
        """
        return self._upload_time

    @upload_time.setter
    def upload_time(self, upload_time: str):
        """Sets the upload_time of this Exercise.

        Time of the transfer from wrist unit to Polar database  # noqa: E501

        :param upload_time: The upload_time of this Exercise.
        :type upload_time: str
        """

        self._upload_time = upload_time

    @property
    def polar_user(self) -> str:
        """Gets the polar_user of this Exercise.

        Absolute link to Polar user owning the training  # noqa: E501

        :return: The polar_user of this Exercise.
        :rtype: str
        """
        return self._polar_user

    @polar_user.setter
    def polar_user(self, polar_user: str):
        """Sets the polar_user of this Exercise.

        Absolute link to Polar user owning the training  # noqa: E501

        :param polar_user: The polar_user of this Exercise.
        :type polar_user: str
        """

        self._polar_user = polar_user

    @property
    def transaction_id(self) -> int:
        """Gets the transaction_id of this Exercise.

        Id of the exercise-transaction this training was transferred in  # noqa: E501

        :return: The transaction_id of this Exercise.
        :rtype: int
        """
        return self._transaction_id

    @transaction_id.setter
    def transaction_id(self, transaction_id: int):
        """Sets the transaction_id of this Exercise.

        Id of the exercise-transaction this training was transferred in  # noqa: E501

        :param transaction_id: The transaction_id of this Exercise.
        :type transaction_id: int
        """

        self._transaction_id = transaction_id

    @property
    def device(self) -> str:
        """Gets the device of this Exercise.

        Polar product used in training  # noqa: E501

        :return: The device of this Exercise.
        :rtype: str
        """
        return self._device

    @device.setter
    def device(self, device: str):
        """Sets the device of this Exercise.

        Polar product used in training  # noqa: E501

        :param device: The device of this Exercise.
        :type device: str
        """

        self._device = device

    @property
    def device_id(self) -> str:
        """Gets the device_id of this Exercise.

        Id of the Polar device  # noqa: E501

        :return: The device_id of this Exercise.
        :rtype: str
        """
        return self._device_id

    @device_id.setter
    def device_id(self, device_id: str):
        """Sets the device_id of this Exercise.

        Id of the Polar device  # noqa: E501

        :param device_id: The device_id of this Exercise.
        :type device_id: str
        """

        self._device_id = device_id

    @property
    def start_time(self) -> str:
        """Gets the start_time of this Exercise.

        Start time of the training session in local time  # noqa: E501

        :return: The start_time of this Exercise.
        :rtype: str
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time: str):
        """Sets the start_time of this Exercise.

        Start time of the training session in local time  # noqa: E501

        :param start_time: The start_time of this Exercise.
        :type start_time: str
        """

        self._start_time = start_time

    @property
    def start_time_utc_offset(self) -> int:
        """Gets the start_time_utc_offset of this Exercise.

        The offset from UTC (in minutes) when the training session was started  # noqa: E501

        :return: The start_time_utc_offset of this Exercise.
        :rtype: int
        """
        return self._start_time_utc_offset

    @start_time_utc_offset.setter
    def start_time_utc_offset(self, start_time_utc_offset: int):
        """Sets the start_time_utc_offset of this Exercise.

        The offset from UTC (in minutes) when the training session was started  # noqa: E501

        :param start_time_utc_offset: The start_time_utc_offset of this Exercise.
        :type start_time_utc_offset: int
        """

        self._start_time_utc_offset = start_time_utc_offset

    @property
    def duration(self) -> str:
        """Gets the duration of this Exercise.

        The duration of the training session as specified in ISO8601  # noqa: E501

        :return: The duration of this Exercise.
        :rtype: str
        """
        return self._duration

    @duration.setter
    def duration(self, duration: str):
        """Sets the duration of this Exercise.

        The duration of the training session as specified in ISO8601  # noqa: E501

        :param duration: The duration of this Exercise.
        :type duration: str
        """

        self._duration = duration

    @property
    def calories(self) -> int:
        """Gets the calories of this Exercise.

        Expended calories during training in kilocalories  # noqa: E501

        :return: The calories of this Exercise.
        :rtype: int
        """
        return self._calories

    @calories.setter
    def calories(self, calories: int):
        """Sets the calories of this Exercise.

        Expended calories during training in kilocalories  # noqa: E501

        :param calories: The calories of this Exercise.
        :type calories: int
        """

        self._calories = calories

    @property
    def distance(self) -> float:
        """Gets the distance of this Exercise.

        Distance in meters travelled during training  # noqa: E501

        :return: The distance of this Exercise.
        :rtype: float
        """
        return self._distance

    @distance.setter
    def distance(self, distance: float):
        """Sets the distance of this Exercise.

        Distance in meters travelled during training  # noqa: E501

        :param distance: The distance of this Exercise.
        :type distance: float
        """

        self._distance = distance

    @property
    def heart_rate(self) -> HeartRate:
        """Gets the heart_rate of this Exercise.


        :return: The heart_rate of this Exercise.
        :rtype: HeartRate
        """
        return self._heart_rate

    @heart_rate.setter
    def heart_rate(self, heart_rate: HeartRate):
        """Sets the heart_rate of this Exercise.


        :param heart_rate: The heart_rate of this Exercise.
        :type heart_rate: HeartRate
        """

        self._heart_rate = heart_rate

    @property
    def training_load(self) -> float:
        """Gets the training_load of this Exercise.

        Training load effect to user  # noqa: E501

        :return: The training_load of this Exercise.
        :rtype: float
        """
        return self._training_load

    @training_load.setter
    def training_load(self, training_load: float):
        """Sets the training_load of this Exercise.

        Training load effect to user  # noqa: E501

        :param training_load: The training_load of this Exercise.
        :type training_load: float
        """

        self._training_load = training_load

    @property
    def sport(self) -> str:
        """Gets the sport of this Exercise.

        Sport name  # noqa: E501

        :return: The sport of this Exercise.
        :rtype: str
        """
        return self._sport

    @sport.setter
    def sport(self, sport: str):
        """Sets the sport of this Exercise.

        Sport name  # noqa: E501

        :param sport: The sport of this Exercise.
        :type sport: str
        """

        self._sport = sport

    @property
    def has_route(self) -> bool:
        """Gets the has_route of this Exercise.

        Boolean indicating if the exercise has route data  # noqa: E501

        :return: The has_route of this Exercise.
        :rtype: bool
        """
        return self._has_route

    @has_route.setter
    def has_route(self, has_route: bool):
        """Sets the has_route of this Exercise.

        Boolean indicating if the exercise has route data  # noqa: E501

        :param has_route: The has_route of this Exercise.
        :type has_route: bool
        """

        self._has_route = has_route

    @property
    def club_id(self) -> int:
        """Gets the club_id of this Exercise.

        Has value if the exercise is from \"Flow For Club\", otherwise not printed. Value -1 indicates that there were errors finding the club  # noqa: E501

        :return: The club_id of this Exercise.
        :rtype: int
        """
        return self._club_id

    @club_id.setter
    def club_id(self, club_id: int):
        """Sets the club_id of this Exercise.

        Has value if the exercise is from \"Flow For Club\", otherwise not printed. Value -1 indicates that there were errors finding the club  # noqa: E501

        :param club_id: The club_id of this Exercise.
        :type club_id: int
        """

        self._club_id = club_id

    @property
    def club_name(self) -> str:
        """Gets the club_name of this Exercise.

        Has value if the exercise is from \"Flow For Club\", otherwise not printed. Value \"Ambiguous club location. Please contact support.\" is printed in case of error (and the club-id is -1).  # noqa: E501

        :return: The club_name of this Exercise.
        :rtype: str
        """
        return self._club_name

    @club_name.setter
    def club_name(self, club_name: str):
        """Sets the club_name of this Exercise.

        Has value if the exercise is from \"Flow For Club\", otherwise not printed. Value \"Ambiguous club location. Please contact support.\" is printed in case of error (and the club-id is -1).  # noqa: E501

        :param club_name: The club_name of this Exercise.
        :type club_name: str
        """

        self._club_name = club_name

    @property
    def detailed_sport_info(self) -> str:
        """Gets the detailed_sport_info of this Exercise.

        String containing the name of a Polar Flow-compatible sport, if one is set for the exercise.  # noqa: E501

        :return: The detailed_sport_info of this Exercise.
        :rtype: str
        """
        return self._detailed_sport_info

    @detailed_sport_info.setter
    def detailed_sport_info(self, detailed_sport_info: str):
        """Sets the detailed_sport_info of this Exercise.

        String containing the name of a Polar Flow-compatible sport, if one is set for the exercise.  # noqa: E501

        :param detailed_sport_info: The detailed_sport_info of this Exercise.
        :type detailed_sport_info: str
        """

        self._detailed_sport_info = detailed_sport_info

    @property
    def fat_percentage(self) -> int:
        """Gets the fat_percentage of this Exercise.

        Fat percentage of exercise calories. Has value if the exercise is from training device supporting Energy sources, otherwise not printed.  # noqa: E501

        :return: The fat_percentage of this Exercise.
        :rtype: int
        """
        return self._fat_percentage

    @fat_percentage.setter
    def fat_percentage(self, fat_percentage: int):
        """Sets the fat_percentage of this Exercise.

        Fat percentage of exercise calories. Has value if the exercise is from training device supporting Energy sources, otherwise not printed.  # noqa: E501

        :param fat_percentage: The fat_percentage of this Exercise.
        :type fat_percentage: int
        """

        self._fat_percentage = fat_percentage

    @property
    def carbohydrate_percentage(self) -> int:
        """Gets the carbohydrate_percentage of this Exercise.

        Carbohydrate percentage of exercise calories. Has value if the exercise is from training device supporting Energy sources, otherwise not printed.  # noqa: E501

        :return: The carbohydrate_percentage of this Exercise.
        :rtype: int
        """
        return self._carbohydrate_percentage

    @carbohydrate_percentage.setter
    def carbohydrate_percentage(self, carbohydrate_percentage: int):
        """Sets the carbohydrate_percentage of this Exercise.

        Carbohydrate percentage of exercise calories. Has value if the exercise is from training device supporting Energy sources, otherwise not printed.  # noqa: E501

        :param carbohydrate_percentage: The carbohydrate_percentage of this Exercise.
        :type carbohydrate_percentage: int
        """

        self._carbohydrate_percentage = carbohydrate_percentage

    @property
    def protein_percentage(self) -> int:
        """Gets the protein_percentage of this Exercise.

        Protein percentage of exercise calories. Has value if the exercise is from training device supporting Energy sources, otherwise not printed.  # noqa: E501

        :return: The protein_percentage of this Exercise.
        :rtype: int
        """
        return self._protein_percentage

    @protein_percentage.setter
    def protein_percentage(self, protein_percentage: int):
        """Sets the protein_percentage of this Exercise.

        Protein percentage of exercise calories. Has value if the exercise is from training device supporting Energy sources, otherwise not printed.  # noqa: E501

        :param protein_percentage: The protein_percentage of this Exercise.
        :type protein_percentage: int
        """

        self._protein_percentage = protein_percentage

    @property
    def running_index(self) -> int:
        """Gets the running_index of this Exercise.

        <a href=\"https://support.polar.com/en/support/tips/Running_Index_feature#\">  Running index</a> is a score automatically calculated every run based on your  heart rate and speed data collected via GPS or stride sensor.  # noqa: E501

        :return: The running_index of this Exercise.
        :rtype: int
        """
        return self._running_index

    @running_index.setter
    def running_index(self, running_index: int):
        """Sets the running_index of this Exercise.

        <a href=\"https://support.polar.com/en/support/tips/Running_Index_feature#\">  Running index</a> is a score automatically calculated every run based on your  heart rate and speed data collected via GPS or stride sensor.  # noqa: E501

        :param running_index: The running_index of this Exercise.
        :type running_index: int
        """

        self._running_index = running_index

    @property
    def training_load_pro(self) -> List[TrainingLoadProSample]:
        """Gets the training_load_pro of this Exercise.


        :return: The training_load_pro of this Exercise.
        :rtype: List[TrainingLoadProSample]
        """
        return self._training_load_pro

    @training_load_pro.setter
    def training_load_pro(self, training_load_pro: List[TrainingLoadProSample]):
        """Sets the training_load_pro of this Exercise.


        :param training_load_pro: The training_load_pro of this Exercise.
        :type training_load_pro: List[TrainingLoadProSample]
        """

        self._training_load_pro = training_load_pro
