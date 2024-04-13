# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.exercise_hash_id import ExerciseHashId  # noqa: E501
from swagger_server.models.exercises_hash_id import ExercisesHashId  # noqa: E501
from swagger_server.test import BaseTestCase


class TestExercisesController(BaseTestCase):
    """ExercisesController integration test stubs"""

    def test_get_exercise_fit_without_transaction(self):
        """Test case for get_exercise_fit_without_transaction

        Get exercise FIT
        """
        response = self.client.open(
            '//v3/exercises/{exerciseId}/fit'.format(exercise_id='exercise_id_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_exercise_gpx_without_transaction(self):
        """Test case for get_exercise_gpx_without_transaction

        Get exercise GPX
        """
        response = self.client.open(
            '//v3/exercises/{exerciseId}/gpx'.format(exercise_id='exercise_id_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_exercise_tcx_without_transaction(self):
        """Test case for get_exercise_tcx_without_transaction

        Get exercise TCX
        """
        response = self.client.open(
            '//v3/exercises/{exerciseId}/tcx'.format(exercise_id='exercise_id_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_exercise_without_transaction(self):
        """Test case for get_exercise_without_transaction

        Get exercise
        """
        query_string = [('samples', true),
                        ('zones', true),
                        ('route', true)]
        response = self.client.open(
            '//v3/exercises/{exerciseId}'.format(exercise_id='exercise_id_example'),
            method='GET',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_list_exercises_without_transaction(self):
        """Test case for list_exercises_without_transaction

        List exercises
        """
        query_string = [('samples', true),
                        ('zones', true),
                        ('route', true)]
        response = self.client.open(
            '//v3/exercises',
            method='GET',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
