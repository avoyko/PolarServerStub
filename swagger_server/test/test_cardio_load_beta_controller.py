# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.cardio_load_schema import CardioLoadSchema  # noqa: E501
from swagger_server.test import BaseTestCase


class TestCardioLoadBetaController(BaseTestCase):
    """CardioLoadBetaController integration test stubs"""

    def test_v3_users_cardio_load_date_get(self):
        """Test case for v3_users_cardio_load_date_get

        Get cardio load by date
        """
        response = self.client.open(
            '//v3/users/cardio-load/{date}'.format(_date='2013-10-20'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_v3_users_cardio_load_date_get_0(self):
        """Test case for v3_users_cardio_load_date_get_0

        Get cardio load by date range
        """
        query_string = [('_from', '2013-10-20'),
                        ('to', '2013-10-20')]
        response = self.client.open(
            '//v3/users/cardio-load/date',
            method='GET',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_v3_users_cardio_load_get(self):
        """Test case for v3_users_cardio_load_get

        List cardio loads
        """
        response = self.client.open(
            '//v3/users/cardio-load/',
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_v3_users_cardio_load_period_days_days_get(self):
        """Test case for v3_users_cardio_load_period_days_days_get

        Get historical data by days
        """
        response = self.client.open(
            '//v3/users/cardio-load/period/days/{days}'.format(days=180),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_v3_users_cardio_load_period_months_months_get(self):
        """Test case for v3_users_cardio_load_period_months_months_get

        Get historical data by months
        """
        response = self.client.open(
            '//v3/users/cardio-load/period/months/{months}'.format(months=6),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
