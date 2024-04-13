import connexion
import six

from swagger_server.models.body_temperature_period import BodyTemperaturePeriod  # noqa: E501
from swagger_server.models.ecg_test_result import EcgTestResult  # noqa: E501
from swagger_server.models.skin_contact_period import SkinContactPeriod  # noqa: E501
from swagger_server.models.skin_temperature import SkinTemperature  # noqa: E501
from swagger_server.models.spo2_test_result import Spo2TestResult  # noqa: E501
from swagger_server import util


def v3_users_biosensing_bodytemperature_get(_from=None, to=None):  # noqa: E501
    """Body temperature data

    Get user&#x27;s body temperature data for last 28 days or for given date range. Maximum date range between from and to cannot be more than 28 days. # noqa: E501

    :param _from: Inclusive start date of range as ISO-8601 date string, example: \&quot;2023-10-01\&quot;
    :type _from: str
    :param to: Inclusive end date of range as ISO-8601 date string, example: \&quot;2023-10-28\&quot;
    :type to: str

    :rtype: List[BodyTemperaturePeriod]
    """
    _from = util.deserialize_date(_from)
    to = util.deserialize_date(to)
    return 'do some magic!'


def v3_users_biosensing_ecg_get(_from=None, to=None):  # noqa: E501
    """Wrist ECG test result data

    Get user&#x27;s wrist ECG test result data for last 28 days or for given date range. Maximum date range between from and to cannot be more than 28 days. # noqa: E501

    :param _from: Inclusive start date of range as ISO-8601 date string, example: \&quot;2023-10-01\&quot;
    :type _from: str
    :param to: Inclusive end date of range as ISO-8601 date string, example: \&quot;2023-10-28\&quot;
    :type to: str

    :rtype: List[EcgTestResult]
    """
    _from = util.deserialize_date(_from)
    to = util.deserialize_date(to)
    return 'do some magic!'


def v3_users_biosensing_skincontacts_get(_from=None, to=None):  # noqa: E501
    """Skin contacts data

    Get user&#x27;s skin contacts data for last 28 days or for given date range. Maximum date range between from and to cannot be more than 28 days. # noqa: E501

    :param _from: Inclusive start date of range as ISO-8601 date string, example: \&quot;2023-10-01\&quot;
    :type _from: str
    :param to: Inclusive end date of range as ISO-8601 date string, example: \&quot;2023-10-28\&quot;
    :type to: str

    :rtype: List[SkinContactPeriod]
    """
    _from = util.deserialize_date(_from)
    to = util.deserialize_date(to)
    return 'do some magic!'


def v3_users_biosensing_skintemperature_get(_from=None, to=None):  # noqa: E501
    """Sleep skin temperature data

    Get user&#x27;s sleep skin temperature data for last 28 days or for given date range. Maximum date range between from and to cannot be more than 28 days. # noqa: E501

    :param _from: Inclusive start date of range as ISO-8601 date string, example: \&quot;2023-10-01\&quot;
    :type _from: str
    :param to: Inclusive end date of range as ISO-8601 date string, example: \&quot;2023-10-28\&quot;
    :type to: str

    :rtype: List[SkinTemperature]
    """
    _from = util.deserialize_date(_from)
    to = util.deserialize_date(to)
    return 'do some magic!'


def v3_users_biosensing_spo2_get(_from=None, to=None):  # noqa: E501
    """SpO2 test result data

    Get user&#x27;s SpO2 test result data for last 28 days or for given date range. Maximum date range between from and to cannot be more than 28 days. # noqa: E501

    :param _from: Inclusive start date of range as ISO-8601 date string, example: \&quot;2023-10-01\&quot;
    :type _from: str
    :param to: Inclusive end date of range as ISO-8601 date string, example: \&quot;2023-10-28\&quot;
    :type to: str

    :rtype: List[Spo2TestResult]
    """
    _from = util.deserialize_date(_from)
    to = util.deserialize_date(to)
    return 'do some magic!'
