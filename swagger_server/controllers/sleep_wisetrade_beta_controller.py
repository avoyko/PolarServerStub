import connexion
import six

from swagger_server.models.alertness import Alertness  # noqa: E501
from swagger_server.models.circadian_bedtime import CircadianBedtime  # noqa: E501
from swagger_server import util


def v3_users_sleepwise_alertness_date_get(_from, to):  # noqa: E501
    """Alertness period data (date range)

    Get user&#x27;s alertness period data for given date range. Maximum date range between from and to cannot be more than 28 days. &lt;a href&#x3D;\&quot;https://support.polar.com/en/polar-sleepwise\&quot;&gt; Supported devices &lt;/a&gt; # noqa: E501

    :param _from: Inclusive start date of range as ISO-8601 date string, example: \&quot;2022-01-01\&quot;
    :type _from: str
    :param to: Inclusive end date of range as ISO-8601 date string, example: \&quot;2022-01-28\&quot;
    :type to: str

    :rtype: List[Alertness]
    """
    _from = util.deserialize_date(_from)
    to = util.deserialize_date(to)
    return 'do some magic!'


def v3_users_sleepwise_alertness_get():  # noqa: E501
    """Alertness period data (last 28 days)

    Get user&#x27;s alertness period data for the last 28 days. &lt;a href&#x3D;\&quot;https://support.polar.com/en/polar-sleepwise\&quot;&gt; Supported devices &lt;/a&gt; # noqa: E501


    :rtype: List[Alertness]
    """
    return 'do some magic!'


def v3_users_sleepwise_circadian_bedtime_date_get(_from, to):  # noqa: E501
    """Circadian bedtime period data (date range)

    Get user&#x27;s circadian bedtime period data for given date range. Maximum date range between from and to cannot be more than 28 days. &lt;a href&#x3D;\&quot;https://support.polar.com/en/polar-sleepwise\&quot;&gt; Supported devices &lt;/a&gt; # noqa: E501

    :param _from: Inclusive start date of range as ISO-8601 date string, example: \&quot;2022-01-01\&quot;
    :type _from: str
    :param to: Inclusive end date of range as ISO-8601 date string, example: \&quot;2022-01-28\&quot;
    :type to: str

    :rtype: List[CircadianBedtime]
    """
    _from = util.deserialize_date(_from)
    to = util.deserialize_date(to)
    return 'do some magic!'


def v3_users_sleepwise_circadian_bedtime_get():  # noqa: E501
    """Circadian bedtime period data (last 28 days)

    Get user&#x27;s circadian bedtime period data for the last 28 days. &lt;a href&#x3D;\&quot;https://support.polar.com/en/polar-sleepwise\&quot;&gt; Supported devices &lt;/a&gt; # noqa: E501


    :rtype: List[CircadianBedtime]
    """
    return 'do some magic!'
