# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.physical_information import PhysicalInformation  # noqa: E501
from swagger_server.models.physical_informations import PhysicalInformations  # noqa: E501
from swagger_server.models.transaction_location import TransactionLocation  # noqa: E501
from swagger_server.test import BaseTestCase


class TestPhysicalInfoController(BaseTestCase):
    """PhysicalInfoController integration test stubs"""

    def test_commit_physical_info_transaction(self):
        """Test case for commit_physical_info_transaction

        Commit transaction
        """
        response = self.client.open(
            '//v3/users/{user-id}/physical-information-transactions/{transaction-id}'.format(transaction_id=789, user_id=56),
            method='PUT')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_create_physical_info_transaction(self):
        """Test case for create_physical_info_transaction

        Create transaction
        """
        response = self.client.open(
            '//v3/users/{user-id}/physical-information-transactions'.format(user_id=56),
            method='POST')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_physical_info(self):
        """Test case for get_physical_info

        Get physical info
        """
        response = self.client.open(
            '//v3/users/{user-id}/physical-information-transactions/{transaction-id}/physical-informations/{physical-info-id}'.format(user_id=56, transaction_id=56, physical_info_id=56),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_list_physical_infos(self):
        """Test case for list_physical_infos

        List physical infos
        """
        response = self.client.open(
            '//v3/users/{user-id}/physical-information-transactions/{transaction-id}'.format(transaction_id=789, user_id=56),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
