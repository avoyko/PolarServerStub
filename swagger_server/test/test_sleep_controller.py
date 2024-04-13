# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.available_sleeps import AvailableSleeps  # noqa: E501
from swagger_server.models.nights import Nights  # noqa: E501
from swagger_server.models.sleep import Sleep  # noqa: E501
from swagger_server.test import BaseTestCase


class TestSleepController(BaseTestCase):
    """SleepController integration test stubs"""

    def test_list_nights(self):
        """Test case for list_nights

        List nights
        """
        response = self.client.open(
            '//v3/users/sleep',
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_v3_users_sleep_available_get(self):
        """Test case for v3_users_sleep_available_get

        Get available sleep times
        """
        response = self.client.open(
            '//v3/users/sleep/available',
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_v3_users_sleep_date_get(self):
        """Test case for v3_users_sleep_date_get

        Get Sleep
        """
        response = self.client.open(
            '//v3/users/sleep/{date}'.format(_date='_date_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
