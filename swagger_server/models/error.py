# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class Error(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, timestamp: datetime=None, status: int=None, error_type: str=None, message: str=None, corr_id: str=None):  # noqa: E501
        """Error - a model defined in Swagger

        :param timestamp: The timestamp of this Error.  # noqa: E501
        :type timestamp: datetime
        :param status: The status of this Error.  # noqa: E501
        :type status: int
        :param error_type: The error_type of this Error.  # noqa: E501
        :type error_type: str
        :param message: The message of this Error.  # noqa: E501
        :type message: str
        :param corr_id: The corr_id of this Error.  # noqa: E501
        :type corr_id: str
        """
        self.swagger_types = {
            'timestamp': datetime,
            'status': int,
            'error_type': str,
            'message': str,
            'corr_id': str
        }

        self.attribute_map = {
            'timestamp': 'timestamp',
            'status': 'status',
            'error_type': 'errorType',
            'message': 'message',
            'corr_id': 'corrId'
        }
        self._timestamp = timestamp
        self._status = status
        self._error_type = error_type
        self._message = message
        self._corr_id = corr_id

    @classmethod
    def from_dict(cls, dikt) -> 'Error':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The error of this Error.  # noqa: E501
        :rtype: Error
        """
        return util.deserialize_model(dikt, cls)

    @property
    def timestamp(self) -> datetime:
        """Gets the timestamp of this Error.

        Timestamp of the error.  # noqa: E501

        :return: The timestamp of this Error.
        :rtype: datetime
        """
        return self._timestamp

    @timestamp.setter
    def timestamp(self, timestamp: datetime):
        """Sets the timestamp of this Error.

        Timestamp of the error.  # noqa: E501

        :param timestamp: The timestamp of this Error.
        :type timestamp: datetime
        """

        self._timestamp = timestamp

    @property
    def status(self) -> int:
        """Gets the status of this Error.

        Http status code  # noqa: E501

        :return: The status of this Error.
        :rtype: int
        """
        return self._status

    @status.setter
    def status(self, status: int):
        """Sets the status of this Error.

        Http status code  # noqa: E501

        :param status: The status of this Error.
        :type status: int
        """

        self._status = status

    @property
    def error_type(self) -> str:
        """Gets the error_type of this Error.

        Error type.  # noqa: E501

        :return: The error_type of this Error.
        :rtype: str
        """
        return self._error_type

    @error_type.setter
    def error_type(self, error_type: str):
        """Sets the error_type of this Error.

        Error type.  # noqa: E501

        :param error_type: The error_type of this Error.
        :type error_type: str
        """

        self._error_type = error_type

    @property
    def message(self) -> str:
        """Gets the message of this Error.

        Human readable error message.  # noqa: E501

        :return: The message of this Error.
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message: str):
        """Sets the message of this Error.

        Human readable error message.  # noqa: E501

        :param message: The message of this Error.
        :type message: str
        """

        self._message = message

    @property
    def corr_id(self) -> str:
        """Gets the corr_id of this Error.

        Correlation id of the response for problem solving and debugging use.  # noqa: E501

        :return: The corr_id of this Error.
        :rtype: str
        """
        return self._corr_id

    @corr_id.setter
    def corr_id(self, corr_id: str):
        """Sets the corr_id of this Error.

        Correlation id of the response for problem solving and debugging use.  # noqa: E501

        :param corr_id: The corr_id of this Error.
        :type corr_id: str
        """

        self._corr_id = corr_id
