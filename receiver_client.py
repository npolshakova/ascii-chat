#!/usr/bin/python3

import socket               # Import socket module
import sys
import termios
import struct
import fcntl
import argparse

# Setup terminal window size
NROWS = 450
NCOLS = 600

def main():
    parser = argparse.ArgumentParser('Socket Receiver for displaying text to termina')
    parser.add_argument('host', help='IP address to get stream from')
    parser.add_argument('port', help='Port to connect on')

    args = parser.parse_args()

    s = socket.socket()         # Create a socket object
    host = args.host # Get local machine name
    port = args.port                # Reserve a port for your service.

    # change tty/pty setting
    winsize = struct.pack("HHHH", NROWS, NCOLS, 0, 0)
    fcntl.ioctl(sys.stdin, termios.TIOCSWINSZ, winsize)

    # change actual window size
    sys.stdout.write("\x1b[8;{rows};{cols}t".format(rows=NROWS, cols=NCOLS))

    while True:
     input('Connect?')
     try:
        s.connect((host, port))
        print('Connected')
        break
     except socket.error as e:
        print('Failed ' + str(e))

    while True:

     try:
        temp = s.recv(400).decode('utf-8')
        sys.stdout.write(temp)
        if temp is None:
           break
     except (KeyboardInterrupt,socket.error):
           s.close                     # Close the socket when done
           s.shutdown(socket.SHUT_RD)
           print('closed')
           break

if __name__ == '__main__':
    main()
