from .models.heartRate import HeartRate
from .models.bloodPressure import BloodPressure
from .models.pulseOximeter import PulseOximeter

def SensorFactory(sensor):
    """ Factory for making sensors """
    sensors = {
        "HR": HeartRate(),
        "BP": BloodPressure(),
        "PO": PulseOximeter()
    }
    return sensors[sensor]