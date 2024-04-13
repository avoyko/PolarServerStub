import connexion
import six

from swagger_server.models.physical_information import PhysicalInformation  # noqa: E501
from swagger_server.models.physical_informations import PhysicalInformations  # noqa: E501
from swagger_server.models.transaction_location import TransactionLocation  # noqa: E501
from swagger_server import util


def commit_physical_info_transaction(transaction_id, user_id):  # noqa: E501
    """Commit transaction

    After successfully retrieving physical information within a transaction, partners are expected to commit the transaction. # noqa: E501

    :param transaction_id: Transaction identifier
    :type transaction_id: int
    :param user_id: User identifier
    :type user_id: int

    :rtype: None
    """
    return 'do some magic!'


def create_physical_info_transaction(user_id):  # noqa: E501
    """Create transaction

    Initiate physical info transaction. Check for new physical info and create a new transaction if found. # noqa: E501

    :param user_id: User identifier
    :type user_id: int

    :rtype: TransactionLocation
    """
    return 'do some magic!'


def get_physical_info(user_id, transaction_id, physical_info_id):  # noqa: E501
    """Get physical info

    Get physical info entity data # noqa: E501

    :param user_id: User identifier
    :type user_id: int
    :param transaction_id: Transaction identifier
    :type transaction_id: int
    :param physical_info_id: Physical information identifier
    :type physical_info_id: int

    :rtype: PhysicalInformation
    """
    return 'do some magic!'


def list_physical_infos(transaction_id, user_id):  # noqa: E501
    """List physical infos

    List new physical info data. After successfully initiating a transaction, physical infos included within it can be retrieved with the provided transactionId. # noqa: E501

    :param transaction_id: Transaction identifier
    :type transaction_id: int
    :param user_id: User identifier
    :type user_id: int

    :rtype: PhysicalInformations
    """
    return 'do some magic!'
