from ..sensorFactory import SensorFactory

class SensorHandler:
    """
    Create some sensor by factory and Operate it
    """
    def __init__(self, sensor="HR"):
        self.sensorHandler = SensorFactory(sensor)

    def execute(self, ID, sleep, seed=0.7, period=4, format='json'):
        self.sensorHandler.connect()
        for _ in range(period):
            self.sensorHandler.read(ID, sleep, seed)
            self.sensorHandler.makeEvent(format)
            self.sensorHandler.send()
        self.sensorHandler.close()