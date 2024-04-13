import connexion
import six

from swagger_server.models.continuous_heartrate import ContinuousHeartrate  # noqa: E501
from swagger_server import util


def v3_users_continuous_heart_rate_date_get(_date):  # noqa: E501
    """Get Continuous Heart rate samples

    Get users continuous heart rate values for given date. &lt;a href&#x3D;\&quot;https://support.polar.com/en/support/the_what_and_how_of_polars_continuous_heart_rate\&quot;&gt; Supported devices &lt;/a&gt; # noqa: E501

    :param _date: Date of Continuous Heart Rate as ISO-8601 date string, example: \&quot;2022-01-01\&quot;
    :type _date: str

    :rtype: ContinuousHeartrate
    """
    _date = util.deserialize_date(_date)
    return 'do some magic!'
