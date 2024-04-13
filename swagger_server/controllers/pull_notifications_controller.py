import connexion
import six

from swagger_server.models.available_user_datas import AvailableUserDatas  # noqa: E501
from swagger_server import util


def list():  # noqa: E501
    """List

    Get list of available exercises and activities for users # noqa: E501


    :rtype: AvailableUserDatas
    """
    return 'do some magic!'
