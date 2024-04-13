# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.available_user_datas import AvailableUserDatas  # noqa: E501
from swagger_server.test import BaseTestCase


class TestPullNotificationsController(BaseTestCase):
    """PullNotificationsController integration test stubs"""

    def test_list(self):
        """Test case for list

        List
        """
        response = self.client.open(
            '//v3/notifications',
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
