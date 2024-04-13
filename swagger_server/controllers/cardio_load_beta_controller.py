import connexion
import six

from swagger_server.models.cardio_load_schema import CardioLoadSchema  # noqa: E501
from swagger_server import util


def v3_users_cardio_load_date_get(_date):  # noqa: E501
    """Get cardio load by date

    Returns cardio load data for selected date. # noqa: E501

    :param _date: Inclusive start date of range as ISO-8601 date string, example: \&quot;2022-01-01\&quot;
    :type _date: str

    :rtype: CardioLoadSchema
    """
    _date = util.deserialize_date(_date)
    return 'do some magic!'


def v3_users_cardio_load_date_get_0(_from, to):  # noqa: E501
    """Get cardio load by date range

    Returns cardio load data for selected date range.  The response list contains cardio load objects for every day between range even if the cardio load values cannot be calculated, in this case the cardio load status is represented as LOAD_STATUS_NOT_AVAILABLE. # noqa: E501

    :param _from: Inclusive as ISO-8601 date string, example: \&quot;2022-01-01\&quot;
    :type _from: str
    :param to: Inclusive as ISO-8601 date string, example: \&quot;2022-01-01\&quot;
    :type to: str

    :rtype: CardioLoadSchema
    """
    _from = util.deserialize_date(_from)
    to = util.deserialize_date(to)
    return 'do some magic!'


def v3_users_cardio_load_get():  # noqa: E501
    """List cardio loads

    Returns cardio load data for the last 28 days. # noqa: E501


    :rtype: CardioLoadSchema
    """
    return 'do some magic!'


def v3_users_cardio_load_period_days_days_get(days):  # noqa: E501
    """Get historical data by days

    Returns historical cardio load data for selected period of days counting from current date. # noqa: E501

    :param days: Period of days.
    :type days: int

    :rtype: CardioLoadSchema
    """
    return 'do some magic!'


def v3_users_cardio_load_period_months_months_get(months):  # noqa: E501
    """Get historical data by months

    Returns historical cardio load data for selected period of months counting from current date. # noqa: E501

    :param months: Period of months.
    :type months: int

    :rtype: CardioLoadSchema
    """
    return 'do some magic!'
