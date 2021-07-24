import socket

def createSocket(family=socket.AF_INET, type=socket.SOCK_STREAM):
    """ Create the socket instance """
    sock = socket.socket(family, type)
    return sock