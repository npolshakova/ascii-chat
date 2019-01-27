#!/usr/bin/python3
import socket
import sys
import argparse

def main():

    parser = argparse.ArgumentParser('Serves data from stdin over TCP')
    parser.add_argument("port", help="port to connect on")
    args = parser.parse_args()
    port = int(args.port)

    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR,1)

    host = ''
    s.bind((host,port))
    s.listen(5)

    while True:
        try:
            try:
                c, addr = s.accept()
                print('ASCII Bridge Connection Accepted')

            except KeyboardInterrupt:
                print('ASCII Bridge Stopped Waiting, Exiting...')
                break
            print('ASCII Bridge Connected with', addr)
            while True:
                data = sys.stdin.readline()
                c.send(bytes(data,'utf-8'))
        except (KeyboardInterrupt,socket.error):
            c.close()
            break
    s.shutdown(socket.SHUT_WR)
    s.close()

if __name__ == '__main__':
    main()
