import socket

class NetworkSocket:
    """ Network for TCP Socket """
    def __init__(self):
        self.sock = None

    def createSocket(self, family=socket.AF_INET, type=socket.SOCK_STREAM):
        """ Create the socket instance
        @param {
            family: socket format (e.g., ipv4, ipv6, etc),
            type: socket type
        }
        """
        self.sock = socket.socket(family, type)
        return self.sock