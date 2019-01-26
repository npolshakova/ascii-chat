#!/usr/bin/python3
import socket
import sys
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR,1)
host = socket.gethostname()
port = 1234
s.bind((host,port))

s.listen(5)
while True:
    try:
        try:
            c, addr = s.accept()

        except KeyboardInterrupt:
            # print('Stopped Waiting, Exiting...')
            break
        # print 'Connected with', addr
        while True:
            data = sys.stdin.read(10)
            #print('Read some data' + data)
            c.send(str(data))
    except (KeyboardInterrupt,socket.error):
        c.close()
        # print('Connection Closed')
        break
s.shutdown(socket.SHUT_WR)
s.close()
