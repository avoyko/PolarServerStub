# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server.models.webhook_type import WebhookType  # noqa: F401,E501
from swagger_server import util


class WebhookPatch(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, events: List[WebhookType]=None, url: str=None):  # noqa: E501
        """WebhookPatch - a model defined in Swagger

        :param events: The events of this WebhookPatch.  # noqa: E501
        :type events: List[WebhookType]
        :param url: The url of this WebhookPatch.  # noqa: E501
        :type url: str
        """
        self.swagger_types = {
            'events': List[WebhookType],
            'url': str
        }

        self.attribute_map = {
            'events': 'events',
            'url': 'url'
        }
        self._events = events
        self._url = url

    @classmethod
    def from_dict(cls, dikt) -> 'WebhookPatch':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The webhookPatch of this WebhookPatch.  # noqa: E501
        :rtype: WebhookPatch
        """
        return util.deserialize_model(dikt, cls)

    @property
    def events(self) -> List[WebhookType]:
        """Gets the events of this WebhookPatch.

        Type of events to subscribe.  # noqa: E501

        :return: The events of this WebhookPatch.
        :rtype: List[WebhookType]
        """
        return self._events

    @events.setter
    def events(self, events: List[WebhookType]):
        """Sets the events of this WebhookPatch.

        Type of events to subscribe.  # noqa: E501

        :param events: The events of this WebhookPatch.
        :type events: List[WebhookType]
        """

        self._events = events

    @property
    def url(self) -> str:
        """Gets the url of this WebhookPatch.

        Url where the webhook notification is sent.  # noqa: E501

        :return: The url of this WebhookPatch.
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url: str):
        """Sets the url of this WebhookPatch.

        Url where the webhook notification is sent.  # noqa: E501

        :param url: The url of this WebhookPatch.
        :type url: str
        """

        self._url = url
