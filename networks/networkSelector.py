from .mqtt.subscriber import Subscribe
from .mqtt.publisher import Publisher
from .socket.client import NetworkSocket

def NetworkSelector(protocol="socket"):
    networks = {
        "socket": NetworkSocket(),
        "mqttSub": Subscribe(),
        "mqttPub": Publisher()
    }
    return networks[protocol]
