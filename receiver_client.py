#!/usr/bin/python3

import time
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

    s = socket.socket()
    host = args.host
    port = int(args.port)

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
        prev_time = time.time()
        try:
            if time.time() - prev_time > 1:
                prev_time = time.time()
                sys.stdout.write('\033[2J')
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
