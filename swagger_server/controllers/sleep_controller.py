import connexion
import six

from swagger_server.models.available_sleeps import AvailableSleeps  # noqa: E501
from swagger_server.models.nights import Nights  # noqa: E501
from swagger_server.models.sleep import Sleep  # noqa: E501
from swagger_server import util


def list_nights():  # noqa: E501
    """List nights

    List sleep data of user for the last 28 days. # noqa: E501


    :rtype: Nights
    """
    return 'do some magic!'


def v3_users_sleep_available_get():  # noqa: E501
    """Get available sleep times

    Get the dates with sleep start and end times, where user has sleep data available in the last 28 days. # noqa: E501


    :rtype: AvailableSleeps
    """
    return 'do some magic!'


def v3_users_sleep_date_get(_date):  # noqa: E501
    """Get Sleep

    Get Users sleep data for given date. # noqa: E501

    :param _date: Date of sleep as ISO-8601 date string, example: \&quot;2020-01-01\&quot;
    :type _date: str

    :rtype: Sleep
    """
    return 'do some magic!'
