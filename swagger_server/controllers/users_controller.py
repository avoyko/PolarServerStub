import connexion
import six

from swagger_server.models.register import Register  # noqa: E501
from swagger_server.models.user import User  # noqa: E501
from swagger_server import util


def delete_user(user_id):  # noqa: E501
    """Delete user

    When partner wishes no longer to receive user data, user can be de-registered.This will revoke the access token authorized by user. # noqa: E501

    :param user_id: User identifier
    :type user_id: int

    :rtype: None
    """
    return 'do some magic!'


def get_user_information(user_id):  # noqa: E501
    """Get user information

    List user basic information. Note: Although it is possible to get users weight and height from this resource, the [get physical info](#get-physical-info) should be used instead. # noqa: E501

    :param user_id: User identifier
    :type user_id: int

    :rtype: User
    """
    return 'do some magic!'


def register_user(body):  # noqa: E501
    """Register user

    Once partner has been authorized by user, partner must register the user before being able to access its data. API user-id and Polar User Id (polar-user-id) are interchangeable terms. # noqa: E501

    :param body: 
    :type body: dict | bytes

    :rtype: User
    """
    if connexion.request.is_json:
        body = Register.from_dict(connexion.request.get_json())  # noqa: E501
    return User(6111166)
