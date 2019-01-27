#!/usr/bin/python3
import socket

UDP_IP = "127.0.0.1"
UDP_PORT = 5005

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # Internet #UDP

sock.bind(('', UDP_PORT))

while True:
    data, addr = sock.recvfrom(16)
    print("received message:", data)
