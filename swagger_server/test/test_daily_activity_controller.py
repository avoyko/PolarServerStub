# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.activity import Activity  # noqa: E501
from swagger_server.models.activity_log import ActivityLog  # noqa: E501
from swagger_server.models.activity_step_samples import ActivityStepSamples  # noqa: E501
from swagger_server.models.activity_zone_samples import ActivityZoneSamples  # noqa: E501
from swagger_server.models.transaction_location import TransactionLocation  # noqa: E501
from swagger_server.test import BaseTestCase


class TestDailyActivityController(BaseTestCase):
    """DailyActivityController integration test stubs"""

    def test_commit_activity_transaction(self):
        """Test case for commit_activity_transaction

        Commit transaction
        """
        response = self.client.open(
            '//v3/users/{user-id}/activity-transactions/{transaction-id}'.format(transaction_id=789, user_id=56),
            method='PUT')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_create_activity_transaction(self):
        """Test case for create_activity_transaction

        Create transaction
        """
        response = self.client.open(
            '//v3/users/{user-id}/activity-transactions'.format(user_id=56),
            method='POST')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_activity_summary(self):
        """Test case for get_activity_summary

        Get activity summary
        """
        response = self.client.open(
            '//v3/users/{user-id}/activity-transactions/{transaction-id}/activities/{activity-id}'.format(user_id=56, transaction_id=56, activity_id=56),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_step_samples(self):
        """Test case for get_step_samples

        Get step samples
        """
        response = self.client.open(
            '//v3/users/{user-id}/activity-transactions/{transaction-id}/activities/{activity-id}/step-samples'.format(user_id=56, transaction_id=56, activity_id=56),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_zone_samples(self):
        """Test case for get_zone_samples

        Get zone samples
        """
        response = self.client.open(
            '//v3/users/{user-id}/activity-transactions/{transaction-id}/activities/{activity-id}/zone-samples'.format(user_id=56, transaction_id=56, activity_id=56),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_list_activities(self):
        """Test case for list_activities

        List activities
        """
        response = self.client.open(
            '//v3/users/{user-id}/activity-transactions/{transaction-id}'.format(transaction_id=789, user_id=56),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
