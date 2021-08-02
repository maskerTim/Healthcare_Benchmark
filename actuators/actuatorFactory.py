from .models.heartActuator import HeartActuator

def ActuatorFactory(actuator):
    """ Factory for making sensors """
    actuators = {
        "HA": HeartActuator()
    }
    return actuators[actuator]