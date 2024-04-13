import connexion
import six

from swagger_server.models.created_webhook import CreatedWebhook  # noqa: E501
from swagger_server.models.error import Error  # noqa: E501
from swagger_server.models.webhook_info import WebhookInfo  # noqa: E501
from swagger_server.models.webhook_patch import WebhookPatch  # noqa: E501
from swagger_server.models.webhook_request import WebhookRequest  # noqa: E501
from swagger_server import util


def create_webhook(body):  # noqa: E501
    """Create webhook

    Create new webhook.  When creating webhook the AccessLink sends a ping message to the url in request body. The ping message must be answered with 200 OK or otherwise the webhook is not created.  Created webhook is by default in activated state and will send push notifications about subscribed events. Webhook will be automatically deactivated if push notifications have not been successful for a period of seven (7) days. **Note!** Save the *signature_secret_key* from response since this is the only chance to get it. # noqa: E501

    :param body: Webhook to create.
    :type body: dict | bytes

    :rtype: CreatedWebhook
    """
    if connexion.request.is_json:
        body = WebhookRequest.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def delete_webhook(webhook_id):  # noqa: E501
    """Delete webhook

    Delete webhook by id. # noqa: E501

    :param webhook_id: Webhook id to delete
    :type webhook_id: str

    :rtype: None
    """
    return 'do some magic!'


def get_webhook():  # noqa: E501
    """Get webhook

    Returns created webhook if exists. # noqa: E501


    :rtype: WebhookInfo
    """
    return 'do some magic!'


def update_webhook(body, webhook_id):  # noqa: E501
    """Update webhook

    Edit webhook event types and/or url.  When updating webhook url the AccessLink sends a ping message to the new address. The ping message must be answered with 200 OK or otherwise the webhook is not updated. # noqa: E501

    :param body: New value(s) for events and/or url.
    :type body: dict | bytes
    :param webhook_id: Webhook id to update
    :type webhook_id: str

    :rtype: WebhookInfo
    """
    if connexion.request.is_json:
        body = WebhookPatch.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def v3_webhooks_activate_post():  # noqa: E501
    """Activate webhook

    Activate deactivated webhook. Activation is successful if the configured webhook url returns HTTP status 200 (OK) for the issued ping request. # noqa: E501


    :rtype: None
    """
    return 'do some magic!'


def v3_webhooks_deactivate_post():  # noqa: E501
    """Deactivate webhook

    Deactivate activated webhook. Deactivated webhook does not push notifications about subscribed events. # noqa: E501


    :rtype: None
    """
    return 'do some magic!'
