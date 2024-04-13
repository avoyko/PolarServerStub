# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class TrainingLoadProRpeEnum(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    allowed enum values
    """
    UNKNOWN = "UNKNOWN"
    RPE_NONE = "RPE_NONE"
    RPE_EASY = "RPE_EASY"
    RPE_LIGHT = "RPE_LIGHT"
    RPE_FAIRLY_BRISK = "RPE_FAIRLY_BRISK"
    RPE_BRISK = "RPE_BRISK"
    RPE_MODERATE = "RPE_MODERATE"
    RPE_FAIRLY_HARD = "RPE_FAIRLY_HARD"
    RPE_HARD = "RPE_HARD"
    RPE_EXHAUSTING = "RPE_EXHAUSTING"
    RPE_EXTREME = "RPE_EXTREME"
    def __init__(self):  # noqa: E501
        """TrainingLoadProRpeEnum - a model defined in Swagger

        """
        self.swagger_types = {
        }

        self.attribute_map = {
        }

    @classmethod
    def from_dict(cls, dikt) -> 'TrainingLoadProRpeEnum':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The training-load-pro-rpe-enum of this TrainingLoadProRpeEnum.  # noqa: E501
        :rtype: TrainingLoadProRpeEnum
        """
        return util.deserialize_model(dikt, cls)
