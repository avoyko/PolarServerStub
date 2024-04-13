# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server.models.webhook_info_data import WebhookInfoData  # noqa: F401,E501
from swagger_server import util


class WebhookInfo(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, data: WebhookInfoData=None):  # noqa: E501
        """WebhookInfo - a model defined in Swagger

        :param data: The data of this WebhookInfo.  # noqa: E501
        :type data: WebhookInfoData
        """
        self.swagger_types = {
            'data': WebhookInfoData
        }

        self.attribute_map = {
            'data': 'data'
        }
        self._data = data

    @classmethod
    def from_dict(cls, dikt) -> 'WebhookInfo':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The webhookInfo of this WebhookInfo.  # noqa: E501
        :rtype: WebhookInfo
        """
        return util.deserialize_model(dikt, cls)

    @property
    def data(self) -> WebhookInfoData:
        """Gets the data of this WebhookInfo.


        :return: The data of this WebhookInfo.
        :rtype: WebhookInfoData
        """
        return self._data

    @data.setter
    def data(self, data: WebhookInfoData):
        """Sets the data of this WebhookInfo.


        :param data: The data of this WebhookInfo.
        :type data: WebhookInfoData
        """

        self._data = data
