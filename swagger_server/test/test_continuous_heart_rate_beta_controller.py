# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.continuous_heartrate import ContinuousHeartrate  # noqa: E501
from swagger_server.test import BaseTestCase


class TestContinuousHeartRateBetaController(BaseTestCase):
    """ContinuousHeartRateBetaController integration test stubs"""

    def test_v3_users_continuous_heart_rate_get(self):
        """Test case for v3_users_continuous_heart_rate_get

        Get Continuous Heart rate samples with range
        """
        query_string = [('_from', '2013-10-20'),
                        ('to', '2013-10-20')]
        response = self.client.open(
            '//v3/users/continuous-heart-rate',
            method='GET',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
