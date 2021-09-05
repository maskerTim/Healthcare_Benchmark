from .models.heartRate import HeartRate
from .models.bloodPressure import BloodPressure
from .models.pulseOximeter import PulseOximeter
from .models.foreheadTemperature import ForeheadTemperature


def SensorFactory(sensor):
    """ Factory for making sensors """
    sensors = {
        "HR": HeartRate(),
        "BP": BloodPressure(),
        "PO": PulseOximeter(),
        "FT": ForeheadTemperature()
    }
    return sensors[sensor]
