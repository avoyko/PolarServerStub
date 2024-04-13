# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class Samples(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, samples: List[str]=None):  # noqa: E501
        """Samples - a model defined in Swagger

        :param samples: The samples of this Samples.  # noqa: E501
        :type samples: List[str]
        """
        self.swagger_types = {
            'samples': List[str]
        }

        self.attribute_map = {
            'samples': 'samples'
        }
        self._samples = samples

    @classmethod
    def from_dict(cls, dikt) -> 'Samples':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The samples of this Samples.  # noqa: E501
        :rtype: Samples
        """
        return util.deserialize_model(dikt, cls)

    @property
    def samples(self) -> List[str]:
        """Gets the samples of this Samples.

        List of URIs pointing to single sample type data.  # noqa: E501

        :return: The samples of this Samples.
        :rtype: List[str]
        """
        return self._samples

    @samples.setter
    def samples(self, samples: List[str]):
        """Sets the samples of this Samples.

        List of URIs pointing to single sample type data.  # noqa: E501

        :param samples: The samples of this Samples.
        :type samples: List[str]
        """

        self._samples = samples
