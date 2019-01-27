#!/usr/bin/python3
import socket
import sys
import argparse

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR,1)

#host = socket.gethostname()
host = ''

parser = argparse.ArgumentParser("Socket Port")
parser.add_argument("port", help="port to connect on")
args = parser.parse_args()
port = int(args.port)

s.bind((host,port))

s.listen(5)
while True:
    try:
        try:
            c, addr = s.accept()
            #print('accepted')

        except KeyboardInterrupt:
            # print('Stopped Waiting, Exiting...')
            break
        # print 'Connected with', addr
        while True:
            #print('reading stdin')
            #data = sys.stdin.read(10)
            data = sys.stdin.readline()
            #print(data)
            #print('Read some data' + data)
            c.send(bytes(data,'utf-8'))
    except (KeyboardInterrupt,socket.error):
        c.close()
        # print('Connection Closed')
        break
s.shutdown(socket.SHUT_WR)
s.close()
