import connexion
import six

from swagger_server.models.nightly_recharge import NightlyRecharge  # noqa: E501
from swagger_server.models.recharges import Recharges  # noqa: E501
from swagger_server import util


def list_nightly_recharge():  # noqa: E501
    """List Nightly Recharges

    List Nightly Recharge data of user for the last 28 days. # noqa: E501


    :rtype: Recharges
    """
    return 'do some magic!'


def v3_users_nightly_recharge_date_get(_date):  # noqa: E501
    """Get Nightly Recharge

    Get Users Nightly Recharge data for given date. # noqa: E501

    :param _date: Date of Nightly Recharge as ISO-8601 date string, example: \&quot;2020-01-01\&quot;
    :type _date: str

    :rtype: NightlyRecharge
    """
    return 'do some magic!'
