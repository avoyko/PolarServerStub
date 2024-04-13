# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.nightly_recharge import NightlyRecharge  # noqa: E501
from swagger_server.models.recharges import Recharges  # noqa: E501
from swagger_server.test import BaseTestCase


class TestNightlyRechargeController(BaseTestCase):
    """NightlyRechargeController integration test stubs"""

    def test_list_nightly_recharge(self):
        """Test case for list_nightly_recharge

        List Nightly Recharges
        """
        response = self.client.open(
            '//v3/users/nightly-recharge',
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_v3_users_nightly_recharge_date_get(self):
        """Test case for v3_users_nightly_recharge_date_get

        Get Nightly Recharge
        """
        response = self.client.open(
            '//v3/users/nightly-recharge/{date}'.format(_date='_date_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
