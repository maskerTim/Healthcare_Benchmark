class ActuatorHandler:
    """ operate for actuators """

    def __init__(self, actuator):
        self.actuatorhandler = actuator

    def register(self, actuator):
        """ register the actuator """
        self.actuatorhandler = actuator

    def execute(self, ip, port, protocol):
        """ run actuator """
        # if connect successfully, it will automatically subscribe
        self.actuatorhandler.connect(ip, port, protocol)
