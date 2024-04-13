# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.created_webhook import CreatedWebhook  # noqa: E501
from swagger_server.models.error import Error  # noqa: E501
from swagger_server.models.webhook_info import WebhookInfo  # noqa: E501
from swagger_server.models.webhook_patch import WebhookPatch  # noqa: E501
from swagger_server.models.webhook_request import WebhookRequest  # noqa: E501
from swagger_server.test import BaseTestCase


class TestWebhooksController(BaseTestCase):
    """WebhooksController integration test stubs"""

    def test_create_webhook(self):
        """Test case for create_webhook

        Create webhook
        """
        body = WebhookRequest()
        response = self.client.open(
            '//v3/webhooks',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_delete_webhook(self):
        """Test case for delete_webhook

        Delete webhook
        """
        response = self.client.open(
            '//v3/webhooks/{webhook-id}'.format(webhook_id='webhook_id_example'),
            method='DELETE')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_webhook(self):
        """Test case for get_webhook

        Get webhook
        """
        response = self.client.open(
            '//v3/webhooks',
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_update_webhook(self):
        """Test case for update_webhook

        Update webhook
        """
        body = WebhookPatch()
        response = self.client.open(
            '//v3/webhooks/{webhook-id}'.format(webhook_id='webhook_id_example'),
            method='PATCH',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_v3_webhooks_activate_post(self):
        """Test case for v3_webhooks_activate_post

        Activate webhook
        """
        response = self.client.open(
            '//v3/webhooks/activate',
            method='POST')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_v3_webhooks_deactivate_post(self):
        """Test case for v3_webhooks_deactivate_post

        Deactivate webhook
        """
        response = self.client.open(
            '//v3/webhooks/deactivate',
            method='POST')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
