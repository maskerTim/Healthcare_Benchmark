from .models.heartActuator import HeartActuator
from .models.bloodPressureActuator import BloodPressureActuator

def ActuatorFactory(actuator):
    """ Factory for making sensors """
    actuators = {
        "HA": HeartActuator(),
        "BA": BloodPressureActuator()
    }
    return actuators[actuator]
