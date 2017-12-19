#! /usr/bin/env python
import socket

target_host = "127.0.0.1"
target_port = 5005
buffer_size = 1024
message = "Hello, you sweet, sweet bastard"

#create a socket object
client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

#send some data
client.sendto("AAABBBCCC", (target_host, target_port))

#receive some data
data, addr = client.recvfrom(4096)

print data
