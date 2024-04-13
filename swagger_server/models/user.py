# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server.models.user_extra_info import UserExtraInfo  # noqa: F401,E501
from swagger_server import util


class User(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, polar_user_id: int=None, member_id: str=None, registration_date: datetime=None, first_name: str=None, last_name: str=None, birthdate: str=None, gender: str=None, weight: float=None, height: float=None, extra_info: List[UserExtraInfo]=None):  # noqa: E501
        """User - a model defined in Swagger

        :param polar_user_id: The polar_user_id of this User.  # noqa: E501
        :type polar_user_id: int
        :param member_id: The member_id of this User.  # noqa: E501
        :type member_id: str
        :param registration_date: The registration_date of this User.  # noqa: E501
        :type registration_date: datetime
        :param first_name: The first_name of this User.  # noqa: E501
        :type first_name: str
        :param last_name: The last_name of this User.  # noqa: E501
        :type last_name: str
        :param birthdate: The birthdate of this User.  # noqa: E501
        :type birthdate: str
        :param gender: The gender of this User.  # noqa: E501
        :type gender: str
        :param weight: The weight of this User.  # noqa: E501
        :type weight: float
        :param height: The height of this User.  # noqa: E501
        :type height: float
        :param extra_info: The extra_info of this User.  # noqa: E501
        :type extra_info: List[UserExtraInfo]
        """
        self.swagger_types = {
            'polar_user_id': int,
            'member_id': str,
            'registration_date': datetime,
            'first_name': str,
            'last_name': str,
            'birthdate': str,
            'gender': str,
            'weight': float,
            'height': float,
            'extra_info': List[UserExtraInfo]
        }

        self.attribute_map = {
            'polar_user_id': 'polar-user-id',
            'member_id': 'member-id',
            'registration_date': 'registration-date',
            'first_name': 'first-name',
            'last_name': 'last-name',
            'birthdate': 'birthdate',
            'gender': 'gender',
            'weight': 'weight',
            'height': 'height',
            'extra_info': 'extra-info'
        }
        self._polar_user_id = polar_user_id
        self._member_id = member_id
        self._registration_date = registration_date
        self._first_name = first_name
        self._last_name = last_name
        self._birthdate = birthdate
        self._gender = gender
        self._weight = weight
        self._height = height
        self._extra_info = extra_info

    @classmethod
    def from_dict(cls, dikt) -> 'User':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The user of this User.  # noqa: E501
        :rtype: User
        """
        return util.deserialize_model(dikt, cls)

    @property
    def polar_user_id(self) -> int:
        """Gets the polar_user_id of this User.

        User's id in Polar database  # noqa: E501

        :return: The polar_user_id of this User.
        :rtype: int
        """
        return self._polar_user_id

    @polar_user_id.setter
    def polar_user_id(self, polar_user_id: int):
        """Sets the polar_user_id of this User.

        User's id in Polar database  # noqa: E501

        :param polar_user_id: The polar_user_id of this User.
        :type polar_user_id: int
        """

        self._polar_user_id = polar_user_id

    @property
    def member_id(self) -> str:
        """Gets the member_id of this User.

        User's identifier in partner's database  # noqa: E501

        :return: The member_id of this User.
        :rtype: str
        """
        return self._member_id

    @member_id.setter
    def member_id(self, member_id: str):
        """Sets the member_id of this User.

        User's identifier in partner's database  # noqa: E501

        :param member_id: The member_id of this User.
        :type member_id: str
        """

        self._member_id = member_id

    @property
    def registration_date(self) -> datetime:
        """Gets the registration_date of this User.

        Timestamp marked when ACCEPTED  # noqa: E501

        :return: The registration_date of this User.
        :rtype: datetime
        """
        return self._registration_date

    @registration_date.setter
    def registration_date(self, registration_date: datetime):
        """Sets the registration_date of this User.

        Timestamp marked when ACCEPTED  # noqa: E501

        :param registration_date: The registration_date of this User.
        :type registration_date: datetime
        """

        self._registration_date = registration_date

    @property
    def first_name(self) -> str:
        """Gets the first_name of this User.

        User's first name  # noqa: E501

        :return: The first_name of this User.
        :rtype: str
        """
        return self._first_name

    @first_name.setter
    def first_name(self, first_name: str):
        """Sets the first_name of this User.

        User's first name  # noqa: E501

        :param first_name: The first_name of this User.
        :type first_name: str
        """

        self._first_name = first_name

    @property
    def last_name(self) -> str:
        """Gets the last_name of this User.

        User's surname  # noqa: E501

        :return: The last_name of this User.
        :rtype: str
        """
        return self._last_name

    @last_name.setter
    def last_name(self, last_name: str):
        """Sets the last_name of this User.

        User's surname  # noqa: E501

        :param last_name: The last_name of this User.
        :type last_name: str
        """

        self._last_name = last_name

    @property
    def birthdate(self) -> str:
        """Gets the birthdate of this User.

        User's birthdate as YYYY-MM-DD  # noqa: E501

        :return: The birthdate of this User.
        :rtype: str
        """
        return self._birthdate

    @birthdate.setter
    def birthdate(self, birthdate: str):
        """Sets the birthdate of this User.

        User's birthdate as YYYY-MM-DD  # noqa: E501

        :param birthdate: The birthdate of this User.
        :type birthdate: str
        """

        self._birthdate = birthdate

    @property
    def gender(self) -> str:
        """Gets the gender of this User.

        User's sex  # noqa: E501

        :return: The gender of this User.
        :rtype: str
        """
        return self._gender

    @gender.setter
    def gender(self, gender: str):
        """Sets the gender of this User.

        User's sex  # noqa: E501

        :param gender: The gender of this User.
        :type gender: str
        """
        allowed_values = ["MALE", "FEMALE"]  # noqa: E501
        if gender not in allowed_values:
            raise ValueError(
                "Invalid value for `gender` ({0}), must be one of {1}"
                .format(gender, allowed_values)
            )

        self._gender = gender

    @property
    def weight(self) -> float:
        """Gets the weight of this User.

        User's weight in kg  # noqa: E501

        :return: The weight of this User.
        :rtype: float
        """
        return self._weight

    @weight.setter
    def weight(self, weight: float):
        """Sets the weight of this User.

        User's weight in kg  # noqa: E501

        :param weight: The weight of this User.
        :type weight: float
        """

        self._weight = weight

    @property
    def height(self) -> float:
        """Gets the height of this User.

        Users height in centimeters  # noqa: E501

        :return: The height of this User.
        :rtype: float
        """
        return self._height

    @height.setter
    def height(self, height: float):
        """Sets the height of this User.

        Users height in centimeters  # noqa: E501

        :param height: The height of this User.
        :type height: float
        """

        self._height = height

    @property
    def extra_info(self) -> List[UserExtraInfo]:
        """Gets the extra_info of this User.

        List containing answers given by the user to a number of partner-specific questions. Extra-info is null if there are no required fields defined by the partner.  # noqa: E501

        :return: The extra_info of this User.
        :rtype: List[UserExtraInfo]
        """
        return self._extra_info

    @extra_info.setter
    def extra_info(self, extra_info: List[UserExtraInfo]):
        """Sets the extra_info of this User.

        List containing answers given by the user to a number of partner-specific questions. Extra-info is null if there are no required fields defined by the partner.  # noqa: E501

        :param extra_info: The extra_info of this User.
        :type extra_info: List[UserExtraInfo]
        """

        self._extra_info = extra_info
