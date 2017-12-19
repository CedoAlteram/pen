#! /usr/bin/env python

import socket

TCP_IP = '127.0.0.1'
TCP_PORT = 9999
BUFFER_SIZE = 1024
MESSAGE = 'Hello, you sweet, sweet bastard'

#create a socket object, socket.AF_INET says we are going to use a standard IPv4 address or hostname
#SOCK_STREAM indicates that this will be a TCP client
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#connect the client
client.connect((TCP_IP, TCP_PORT))

#send some data
client.send(MESSAGE)
data = client.recv(BUFFER_SIZE)
client.close()

print 'received data:', data
