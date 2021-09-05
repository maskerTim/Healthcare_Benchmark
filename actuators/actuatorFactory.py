from .models.heartActuator import HeartActuator
from .models.bloodPressureActuator import BloodPressureActuator
from .models.videoActuator import VideoActuator


def ActuatorFactory(actuator):
    """ Factory for making sensors """
    actuators = {
        "HA": HeartActuator(),
        "BA": BloodPressureActuator(),
        "VA": VideoActuator()
    }
    return actuators[actuator]
