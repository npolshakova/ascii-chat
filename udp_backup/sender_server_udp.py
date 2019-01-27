#!/usr/bin/python3
import socket
import sys
s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR,1)
#host = socket.gethostname()
host = '172.18.141.60'
port = 1234

while True:
    try:
        data = sys.stdin.readline()
        s.sendto(bytes(data,'utf-8'), (host,port))
    except (KeyboardInterrupt,socket.error):
        # print('Connection Closed')
        break
s.shutdown(socket.SHUT_WR)
s.close()
