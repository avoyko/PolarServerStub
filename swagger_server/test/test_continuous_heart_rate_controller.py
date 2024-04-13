# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.continuous_heartrate import ContinuousHeartrate  # noqa: E501
from swagger_server.test import BaseTestCase


class TestContinuousHeartRateController(BaseTestCase):
    """ContinuousHeartRateController integration test stubs"""

    def test_v3_users_continuous_heart_rate_date_get(self):
        """Test case for v3_users_continuous_heart_rate_date_get

        Get Continuous Heart rate samples
        """
        response = self.client.open(
            '//v3/users/continuous-heart-rate/{date}'.format(_date='2013-10-20'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
