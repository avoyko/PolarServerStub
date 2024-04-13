import connexion
import six

from swagger_server.models.continuous_heartrate import ContinuousHeartrate  # noqa: E501
from swagger_server import util


def v3_users_continuous_heart_rate_get(_from, to):  # noqa: E501
    """Get Continuous Heart rate samples with range

    Get users continuous heart rate values for given date range. &lt;a href&#x3D;\&quot;https://support.polar.com/en/support/the_what_and_how_of_polars_continuous_heart_rate\&quot;&gt; Supported devices &lt;/a&gt; # noqa: E501

    :param _from: Inclusive start date of range as ISO-8601 date string, example: \&quot;2022-01-01\&quot;
    :type _from: str
    :param to: Inclusive end date of range as ISO-8601 date string, example: \&quot;2022-01-28\&quot;
    :type to: str

    :rtype: ContinuousHeartrate
    """
    _from = util.deserialize_date(_from)
    to = util.deserialize_date(to)
    return 'do some magic!'
