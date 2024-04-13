# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.register import Register  # noqa: E501
from swagger_server.models.user import User  # noqa: E501
from swagger_server.test import BaseTestCase


class TestUsersController(BaseTestCase):
    """UsersController integration test stubs"""

    def test_delete_user(self):
        """Test case for delete_user

        Delete user
        """
        response = self.client.open(
            '//v3/users/{user-id}'.format(user_id=789),
            method='DELETE')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_user_information(self):
        """Test case for get_user_information

        Get user information
        """
        response = self.client.open(
            '//v3/users/{user-id}'.format(user_id=789),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_register_user(self):
        """Test case for register_user

        Register user
        """
        body = Register()
        response = self.client.open(
            '//v3/users',
            method='POST',
            data=json.dumps(body),
            content_type='application/xml')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
