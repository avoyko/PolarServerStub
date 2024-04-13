# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class WebhookType(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    allowed enum values
    """
    EXERCISE_SLEEP_CONTINUOUS_HEART_RATE_SLEEP_WISE_CIRCADIAN_BEDTIME_SLEEP_WISE_ALERTNESS = "EXERCISE, SLEEP, CONTINUOUS_HEART_RATE, SLEEP_WISE_CIRCADIAN_BEDTIME, SLEEP_WISE_ALERTNESS"
    def __init__(self):  # noqa: E501
        """WebhookType - a model defined in Swagger

        """
        self.swagger_types = {
        }

        self.attribute_map = {
        }

    @classmethod
    def from_dict(cls, dikt) -> 'WebhookType':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The webhookType of this WebhookType.  # noqa: E501
        :rtype: WebhookType
        """
        return util.deserialize_model(dikt, cls)
