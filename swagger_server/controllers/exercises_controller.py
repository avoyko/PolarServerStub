import connexion
import six

from swagger_server.models.exercise_hash_id import ExerciseHashId  # noqa: E501
from swagger_server.models.exercises_hash_id import ExercisesHashId  # noqa: E501
from swagger_server import util


def get_exercise_fit_without_transaction(exercise_id):  # noqa: E501
    """Get exercise FIT

    FIT file for users exercise. Only Exercises uploaded to Flow in the last 30 days are available. Only exercises that have been uploaded to Flow after the user is registered with your client will be available. See [FIT sport mappings in appendix](#sport-type-mapping-in-fit-files). # noqa: E501

    :param exercise_id: Hashed exercise id.
    :type exercise_id: str

    :rtype: str
    """
    return 'do some magic!'


def get_exercise_gpx_without_transaction(exercise_id):  # noqa: E501
    """Get exercise GPX

    GPX file for users exercise without an AccessLink \&quot;transaction\&quot;. Only Exercises uploaded to Flow in the last 30 days are available. Only exercises that have been uploaded to Flow after the user is registered with your client will be available. # noqa: E501

    :param exercise_id: Hashed exercise id.
    :type exercise_id: str

    :rtype: str
    """
    return 'do some magic!'


def get_exercise_tcx_without_transaction(exercise_id):  # noqa: E501
    """Get exercise TCX

    TCX file for users exercise without an AccessLink \&quot;transaction\&quot;. Only Exercises uploaded to Flow in the last 30 days are available. Only exercises that have been uploaded to Flow after the user is registered with your client will be available. # noqa: E501

    :param exercise_id: Hashed exercise id.
    :type exercise_id: str

    :rtype: str
    """
    return 'do some magic!'


def get_exercise_without_transaction(exercise_id, samples=None, zones=None, route=None):  # noqa: E501
    """Get exercise

    Get users exercise using hashed id. Only Exercises uploaded to Flow in the last 30 days are available. Only exercises that have been uploaded to Flow after the user is registered with your client will be available. Use samples and zones query parameters to return optional samples and zone information of the exercise. # noqa: E501

    :param exercise_id: Hashed exercise id.
    :type exercise_id: str
    :param samples: Return all sample data for this exercise.
    :type samples: bool
    :param zones: Return all zones data for this exercise.
    :type zones: bool
    :param route: Return all route data for this exercise.
    :type route: bool

    :rtype: ExerciseHashId
    """
    return 'do some magic!'


def list_exercises_without_transaction(samples=None, zones=None, route=None):  # noqa: E501
    """List exercises

    List users exercises available in AccessLink. Only Exercises uploaded to Flow in the last 30 days are returned. Only exercises that have been uploaded to Flow after the user is registered with your client will be returned. Use samples and zones query parameters to return optional samples and zone information of the exercises. Training Load Pro data will be included in the exercise object if the exercise is recorded with a specific wrist unit model,  please check [compatible devices](https://www.polar.com/en/smart-coaching/training-load-pro) for more information. # noqa: E501

    :param samples: Return all sample data for this exercise.
    :type samples: bool
    :param zones: Return all zones data for this exercise.
    :type zones: bool
    :param route: Return all route data for this exercise.
    :type route: bool

    :rtype: ExercisesHashId
    """
    return 'do some magic!'
