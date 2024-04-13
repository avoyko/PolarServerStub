# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.body_temperature_period import BodyTemperaturePeriod  # noqa: E501
from swagger_server.models.ecg_test_result import EcgTestResult  # noqa: E501
from swagger_server.models.skin_contact_period import SkinContactPeriod  # noqa: E501
from swagger_server.models.skin_temperature import SkinTemperature  # noqa: E501
from swagger_server.models.spo2_test_result import Spo2TestResult  # noqa: E501
from swagger_server.test import BaseTestCase


class TestElixirtradeBiosensingBetaController(BaseTestCase):
    """ElixirtradeBiosensingBetaController integration test stubs"""

    def test_v3_users_biosensing_bodytemperature_get(self):
        """Test case for v3_users_biosensing_bodytemperature_get

        Body temperature data
        """
        query_string = [('_from', '2013-10-20'),
                        ('to', '2013-10-20')]
        response = self.client.open(
            '//v3/users/biosensing/bodytemperature',
            method='GET',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_v3_users_biosensing_ecg_get(self):
        """Test case for v3_users_biosensing_ecg_get

        Wrist ECG test result data
        """
        query_string = [('_from', '2013-10-20'),
                        ('to', '2013-10-20')]
        response = self.client.open(
            '//v3/users/biosensing/ecg',
            method='GET',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_v3_users_biosensing_skincontacts_get(self):
        """Test case for v3_users_biosensing_skincontacts_get

        Skin contacts data
        """
        query_string = [('_from', '2013-10-20'),
                        ('to', '2013-10-20')]
        response = self.client.open(
            '//v3/users/biosensing/skincontacts',
            method='GET',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_v3_users_biosensing_skintemperature_get(self):
        """Test case for v3_users_biosensing_skintemperature_get

        Sleep skin temperature data
        """
        query_string = [('_from', '2013-10-20'),
                        ('to', '2013-10-20')]
        response = self.client.open(
            '//v3/users/biosensing/skintemperature',
            method='GET',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_v3_users_biosensing_spo2_get(self):
        """Test case for v3_users_biosensing_spo2_get

        SpO2 test result data
        """
        query_string = [('_from', '2013-10-20'),
                        ('to', '2013-10-20')]
        response = self.client.open(
            '//v3/users/biosensing/spo2',
            method='GET',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
