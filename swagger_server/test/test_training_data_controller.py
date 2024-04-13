# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.exercise import Exercise  # noqa: E501
from swagger_server.models.exercises import Exercises  # noqa: E501
from swagger_server.models.sample import Sample  # noqa: E501
from swagger_server.models.samples import Samples  # noqa: E501
from swagger_server.models.transaction_location import TransactionLocation  # noqa: E501
from swagger_server.models.zones import Zones  # noqa: E501
from swagger_server.test import BaseTestCase


class TestTrainingDataController(BaseTestCase):
    """TrainingDataController integration test stubs"""

    def test_commit_exercise_transaction(self):
        """Test case for commit_exercise_transaction

        Commit transaction
        """
        response = self.client.open(
            '//v3/users/{user-id}/exercise-transactions/{transaction-id}'.format(transaction_id=789, user_id=56),
            method='PUT')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_create_exercise_transaction(self):
        """Test case for create_exercise_transaction

        Create transaction
        """
        response = self.client.open(
            '//v3/users/{user-id}/exercise-transactions'.format(user_id=56),
            method='POST')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_available_samples(self):
        """Test case for get_available_samples

        Get available samples
        """
        response = self.client.open(
            '//v3/users/{user-id}/exercise-transactions/{transaction-id}/exercises/{exercise-id}/samples'.format(user_id=56, transaction_id=56, exercise_id=56),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_exercise_summary(self):
        """Test case for get_exercise_summary

        Get exercise summary
        """
        response = self.client.open(
            '//v3/users/{user-id}/exercise-transactions/{transaction-id}/exercises/{exercise-id}'.format(user_id=56, transaction_id=56, exercise_id=56),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_fit(self):
        """Test case for get_fit

        Get FIT
        """
        response = self.client.open(
            '//v3/users/{user-id}/exercise-transactions/{transaction-id}/exercises/{exercise-id}/fit'.format(user_id=56, transaction_id=56, exercise_id=56),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_gpx(self):
        """Test case for get_gpx

        Get GPX
        """
        query_string = [('include_pause_times', false)]
        response = self.client.open(
            '//v3/users/{user-id}/exercise-transactions/{transaction-id}/exercises/{exercise-id}/gpx'.format(user_id=56, transaction_id=56, exercise_id=56),
            method='GET',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_heart_rate_zones(self):
        """Test case for get_heart_rate_zones

        Get heart rate zones
        """
        response = self.client.open(
            '//v3/users/{user-id}/exercise-transactions/{transaction-id}/exercises/{exercise-id}/heart-rate-zones'.format(user_id=56, transaction_id=56, exercise_id=56),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_samples(self):
        """Test case for get_samples

        Get samples
        """
        response = self.client.open(
            '//v3/users/{user-id}/exercise-transactions/{transaction-id}/exercises/{exercise-id}/samples/{type-id}'.format(type_id=B, user_id=56, transaction_id=56, exercise_id=56),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_tcx(self):
        """Test case for get_tcx

        Get TCX
        """
        response = self.client.open(
            '//v3/users/{user-id}/exercise-transactions/{transaction-id}/exercises/{exercise-id}/tcx'.format(user_id=56, transaction_id=56, exercise_id=56),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_list_exercises(self):
        """Test case for list_exercises

        List exercises
        """
        response = self.client.open(
            '//v3/users/{user-id}/exercise-transactions/{transaction-id}'.format(transaction_id=789, user_id=56),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
