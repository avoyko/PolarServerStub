# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.alertness import Alertness  # noqa: E501
from swagger_server.models.circadian_bedtime import CircadianBedtime  # noqa: E501
from swagger_server.test import BaseTestCase


class TestSleepWisetradeBetaController(BaseTestCase):
    """SleepWisetradeBetaController integration test stubs"""

    def test_v3_users_sleepwise_alertness_date_get(self):
        """Test case for v3_users_sleepwise_alertness_date_get

        Alertness period data (date range)
        """
        query_string = [('_from', '2013-10-20'),
                        ('to', '2013-10-20')]
        response = self.client.open(
            '//v3/users/sleepwise/alertness/date',
            method='GET',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_v3_users_sleepwise_alertness_get(self):
        """Test case for v3_users_sleepwise_alertness_get

        Alertness period data (last 28 days)
        """
        response = self.client.open(
            '//v3/users/sleepwise/alertness',
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_v3_users_sleepwise_circadian_bedtime_date_get(self):
        """Test case for v3_users_sleepwise_circadian_bedtime_date_get

        Circadian bedtime period data (date range)
        """
        query_string = [('_from', '2013-10-20'),
                        ('to', '2013-10-20')]
        response = self.client.open(
            '//v3/users/sleepwise/circadian-bedtime/date',
            method='GET',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_v3_users_sleepwise_circadian_bedtime_get(self):
        """Test case for v3_users_sleepwise_circadian_bedtime_get

        Circadian bedtime period data (last 28 days)
        """
        response = self.client.open(
            '//v3/users/sleepwise/circadian-bedtime',
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
