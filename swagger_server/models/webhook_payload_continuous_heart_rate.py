# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class WebhookPayloadContinuousHeartRate(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, event: str=None, user_id: int=None, _date: str=None, timestamp: datetime=None, url: str=None):  # noqa: E501
        """WebhookPayloadContinuousHeartRate - a model defined in Swagger

        :param event: The event of this WebhookPayloadContinuousHeartRate.  # noqa: E501
        :type event: str
        :param user_id: The user_id of this WebhookPayloadContinuousHeartRate.  # noqa: E501
        :type user_id: int
        :param _date: The _date of this WebhookPayloadContinuousHeartRate.  # noqa: E501
        :type _date: str
        :param timestamp: The timestamp of this WebhookPayloadContinuousHeartRate.  # noqa: E501
        :type timestamp: datetime
        :param url: The url of this WebhookPayloadContinuousHeartRate.  # noqa: E501
        :type url: str
        """
        self.swagger_types = {
            'event': str,
            'user_id': int,
            '_date': str,
            'timestamp': datetime,
            'url': str
        }

        self.attribute_map = {
            'event': 'event',
            'user_id': 'user_id',
            '_date': 'date',
            'timestamp': 'timestamp',
            'url': 'url'
        }
        self._event = event
        self._user_id = user_id
        self.__date = _date
        self._timestamp = timestamp
        self._url = url

    @classmethod
    def from_dict(cls, dikt) -> 'WebhookPayloadContinuousHeartRate':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The webhookPayloadContinuousHeartRate of this WebhookPayloadContinuousHeartRate.  # noqa: E501
        :rtype: WebhookPayloadContinuousHeartRate
        """
        return util.deserialize_model(dikt, cls)

    @property
    def event(self) -> str:
        """Gets the event of this WebhookPayloadContinuousHeartRate.

        Type of available data.  # noqa: E501

        :return: The event of this WebhookPayloadContinuousHeartRate.
        :rtype: str
        """
        return self._event

    @event.setter
    def event(self, event: str):
        """Sets the event of this WebhookPayloadContinuousHeartRate.

        Type of available data.  # noqa: E501

        :param event: The event of this WebhookPayloadContinuousHeartRate.
        :type event: str
        """

        self._event = event

    @property
    def user_id(self) -> int:
        """Gets the user_id of this WebhookPayloadContinuousHeartRate.

        Id of the user who has new data.  # noqa: E501

        :return: The user_id of this WebhookPayloadContinuousHeartRate.
        :rtype: int
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id: int):
        """Sets the user_id of this WebhookPayloadContinuousHeartRate.

        Id of the user who has new data.  # noqa: E501

        :param user_id: The user_id of this WebhookPayloadContinuousHeartRate.
        :type user_id: int
        """

        self._user_id = user_id

    @property
    def _date(self) -> str:
        """Gets the _date of this WebhookPayloadContinuousHeartRate.

        Date of the available continuous hr data.  # noqa: E501

        :return: The _date of this WebhookPayloadContinuousHeartRate.
        :rtype: str
        """
        return self.__date

    @_date.setter
    def _date(self, _date: str):
        """Sets the _date of this WebhookPayloadContinuousHeartRate.

        Date of the available continuous hr data.  # noqa: E501

        :param _date: The _date of this WebhookPayloadContinuousHeartRate.
        :type _date: str
        """

        self.__date = _date

    @property
    def timestamp(self) -> datetime:
        """Gets the timestamp of this WebhookPayloadContinuousHeartRate.

        Time when webhook notification is sent.  # noqa: E501

        :return: The timestamp of this WebhookPayloadContinuousHeartRate.
        :rtype: datetime
        """
        return self._timestamp

    @timestamp.setter
    def timestamp(self, timestamp: datetime):
        """Sets the timestamp of this WebhookPayloadContinuousHeartRate.

        Time when webhook notification is sent.  # noqa: E501

        :param timestamp: The timestamp of this WebhookPayloadContinuousHeartRate.
        :type timestamp: datetime
        """

        self._timestamp = timestamp

    @property
    def url(self) -> str:
        """Gets the url of this WebhookPayloadContinuousHeartRate.

        Url to the new available data.  # noqa: E501

        :return: The url of this WebhookPayloadContinuousHeartRate.
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url: str):
        """Sets the url of this WebhookPayloadContinuousHeartRate.

        Url to the new available data.  # noqa: E501

        :param url: The url of this WebhookPayloadContinuousHeartRate.
        :type url: str
        """

        self._url = url
