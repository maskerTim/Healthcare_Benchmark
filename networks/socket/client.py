import socket

def createSocket(family=socket.AF_INET, type=socket.SOCK_STREAM):
    sock = socket.socket(family, type)
    return sock