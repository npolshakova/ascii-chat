import socket
 
UDP_IP = "127.0.0.1"
UDP_PORT = 5005
MESSAGE = bytes("Hello, World!",'utf-8')

sock = socket.socket(socket.AF_INET, # Internet
                      socket.SOCK_DGRAM) # UDP
sock.sendto(MESSAGE, (UDP_IP, UDP_PORT))
