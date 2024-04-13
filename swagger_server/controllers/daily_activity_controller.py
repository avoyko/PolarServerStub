import connexion
import six

from swagger_server.models.activity import Activity  # noqa: E501
from swagger_server.models.activity_log import ActivityLog  # noqa: E501
from swagger_server.models.activity_step_samples import ActivityStepSamples  # noqa: E501
from swagger_server.models.activity_zone_samples import ActivityZoneSamples  # noqa: E501
from swagger_server.models.transaction_location import TransactionLocation  # noqa: E501
from swagger_server import util


def commit_activity_transaction(transaction_id, user_id):  # noqa: E501
    """Commit transaction

    After successfully retrieving activity summary data within a transaction, partners are expected to commit the transaction. # noqa: E501

    :param transaction_id: Transaction identifier
    :type transaction_id: int
    :param user_id: User identifier
    :type user_id: int

    :rtype: None
    """
    return 'do some magic!'


def create_activity_transaction(user_id):  # noqa: E501
    """Create transaction

    Initiate activity transaction. Check for new activity summaries and create a new transaction if found. Only data uploaded to Flow in the last 30 days will be available. Only data that has been uploaded to Flow after the user is registered with your client will be available. # noqa: E501

    :param user_id: User identifier
    :type user_id: int

    :rtype: TransactionLocation
    """
    return 'do some stuff!'


def get_activity_summary(user_id, transaction_id, activity_id):  # noqa: E501
    """Get activity summary

     # noqa: E501

    :param user_id: User identifier
    :type user_id: int
    :param transaction_id: Transaction identifier
    :type transaction_id: int
    :param activity_id: Activity summary identifier
    :type activity_id: int

    :rtype: Activity
    """
    return 'do some magic!'


def get_step_samples(user_id, transaction_id, activity_id):  # noqa: E501
    """Get step samples

    Get activity step samples. Example data can be seen from [appendix](#activity-step-time-series). # noqa: E501

    :param user_id: User identifier
    :type user_id: int
    :param transaction_id: Transaction identifier
    :type transaction_id: int
    :param activity_id: Activity summary identifier
    :type activity_id: int

    :rtype: ActivityStepSamples
    """
    return 'do some magic!'


def get_zone_samples(user_id, transaction_id, activity_id):  # noqa: E501
    """Get zone samples

    Get activity zone samples. Example data can be seen from [appendix](#activity-zone-time-series). # noqa: E501

    :param user_id: User identifier
    :type user_id: int
    :param transaction_id: Transaction identifier
    :type transaction_id: int
    :param activity_id: Activity summary identifier
    :type activity_id: int

    :rtype: ActivityZoneSamples
    """
    return 'do some magic!'


def list_activities(transaction_id, user_id):  # noqa: E501
    """List activities

    List new activity data. After successfully initiating a transaction, activity summaries included within it can be retrieved with the provided transactionId. # noqa: E501

    :param transaction_id: Transaction identifier
    :type transaction_id: int
    :param user_id: User identifier
    :type user_id: int

    :rtype: ActivityLog
    """
    return 'do some magic!'
