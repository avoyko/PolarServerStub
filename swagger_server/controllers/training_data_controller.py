import connexion
import six

from swagger_server.models.exercise import Exercise  # noqa: E501
from swagger_server.models.exercises import Exercises  # noqa: E501
from swagger_server.models.sample import Sample  # noqa: E501
from swagger_server.models.samples import Samples  # noqa: E501
from swagger_server.models.transaction_location import TransactionLocation  # noqa: E501
from swagger_server.models.zones import Zones  # noqa: E501
from swagger_server import util


def commit_exercise_transaction(transaction_id, user_id):  # noqa: E501
    """Commit transaction

    After successfully retrieving training session data within a transaction, partners are expected to commit the transaction. # noqa: E501

    :param transaction_id: Transaction identifier
    :type transaction_id: int
    :param user_id: User identifier
    :type user_id: int

    :rtype: None
    """
    return 'do some magic!'


def create_exercise_transaction(user_id):  # noqa: E501
    """Create transaction

    Check for new training data and create a new transaction if found. Only data uploaded to Flow in the last 30 days will be available. Only data that has been uploaded to Flow after the user is registered with your client will be available. # noqa: E501

    :param user_id: User identifier
    :type user_id: int

    :rtype: TransactionLocation
    """
    return TransactionLocation(122,
    "http://localhost:8080/v3/users/21/exercise-transactions/32")


def get_available_samples(user_id, transaction_id, exercise_id):  # noqa: E501
    """Get available samples

    Retrieve list of links to available samples in training session # noqa: E501

    :param user_id: User identifier
    :type user_id: int
    :param transaction_id: Transaction identifier
    :type transaction_id: int
    :param exercise_id: Exercise identifier
    :type exercise_id: int

    :rtype: Samples
    """
    return Samples()


def get_exercise_summary(user_id, transaction_id, exercise_id):  # noqa: E501
    """Get exercise summary

    Retrieve training session summary data # noqa: E501

    :param user_id: User identifier
    :type user_id: int
    :param transaction_id: Transaction identifier
    :type transaction_id: int
    :param exercise_id: Exercise identifier
    :type exercise_id: int

    :rtype: Exercise
    """
    id = "100"
    upload_time = "2008-10-13T10:40:0.000Z"
    polar_user = "https://www.polaraccesslink/v3/users/61111666"
    transaction_id = "179879"
    device = "Polar M400"
    device_id = "1111AAAA"
    start_time = "2008-10-13T10:40:02"
    start_time_utc_offset = "180"
    duration = "PT2H44M45S"
    calories = "530"
    distance = "1600.2"
    heart_rate = None
    training_load = None
    return Exercise(id, upload_time, polar_user, transaction_id, device, device_id, start_time, start_time_utc_offset,
                    duration, calories, distance, heart_rate, training_load)


def get_fit(user_id, transaction_id, exercise_id):  # noqa: E501
    """Get FIT

    Retrieve exercise in FIT format. See [FIT sport mappings in appendix](#sport-type-mapping-in-fit-files). # noqa: E501

    :param user_id: User identifier
    :type user_id: int
    :param transaction_id: Transaction identifier
    :type transaction_id: int
    :param exercise_id: Exercise identifier
    :type exercise_id: int

    :rtype: str
    """
    return TransactionLocation


def get_gpx(user_id, transaction_id, exercise_id, include_pause_times=None):  # noqa: E501
    """Get GPX

    Retrieve training session summary data in GPX format # noqa: E501

    :param user_id: User identifier
    :type user_id: int
    :param transaction_id: Transaction identifier
    :type transaction_id: int
    :param exercise_id: Exercise identifier
    :type exercise_id: int
    :param include_pause_times: Whether to add pauses as part of the route. Default is false.
    :type include_pause_times: bool

    :rtype: str
    """
    return 'do some magic!'


def get_heart_rate_zones(user_id, transaction_id, exercise_id):  # noqa: E501
    """Get heart rate zones

    Retrieve heart rate zones in training session # noqa: E501

    :param user_id: User identifier
    :type user_id: int
    :param transaction_id: Transaction identifier
    :type transaction_id: int
    :param exercise_id: Exercise identifier
    :type exercise_id: int

    :rtype: Zones
    """
    return 'do some magic!'


def get_samples(type_id, user_id, transaction_id, exercise_id):  # noqa: E501
    """Get samples

    Retrieve sample data of given type # noqa: E501

    :param type_id: Sample type id
    :type type_id: str
    :param user_id: User identifier
    :type user_id: int
    :param transaction_id: Transaction identifier
    :type transaction_id: int
    :param exercise_id: Exercise identifier
    :type exercise_id: int

    :rtype: Sample
    """
    return 'do some magic!'


def get_tcx(user_id, transaction_id, exercise_id):  # noqa: E501
    """Get TCX

    Retrieve exercise in TCX format # noqa: E501

    :param user_id: User identifier
    :type user_id: int
    :param transaction_id: Transaction identifier
    :type transaction_id: int
    :param exercise_id: Exercise identifier
    :type exercise_id: int

    :rtype: str
    """
    return 'do some magic!'


def list_exercises(transaction_id, user_id):  # noqa: E501
    """List exercises

    After successfully initiating a transaction, training sessions included within it can be retrieved with the provided transactionId. # noqa: E501

    :param transaction_id: Transaction identifier
    :type transaction_id: int
    :param user_id: User identifier
    :type user_id: int

    :rtype: Exercises
    """
    return Exercises(["http://localhost:8080/v3/users/12/exercise-transactions/34/exercises/56"])
