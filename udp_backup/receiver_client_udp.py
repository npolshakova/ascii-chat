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

    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    host = args.host # Get local machine name
    port = int(args.port)    # Reserve a port for your service.
    s.bind(('',port))

    # change tty/pty setting
    winsize = struct.pack("HHHH", NROWS, NCOLS, 0, 0)
    fcntl.ioctl(sys.stdin, termios.TIOCSWINSZ, winsize)

    # change actual window size
    sys.stdout.write("\x1b[8;{rows};{cols}t".format(rows=NROWS, cols=NCOLS))


    while True:
        prev_time = time.time()
        try:
            if time.time() - prev_time > 1:
                prev_time = time.time()
                sys.stdout.write('\033[2J')
            temp = s.recvfrom(600)[0]
            temp = temp.decode('utf-8')
            sys.stdout.write(temp)
            if temp is None:
               break
        except (KeyboardInterrupt,socket.error):
            s.close
            s.shutdown(socket.SHUT_RD)
            print('closed')
            break

if __name__ == '__main__':
    main()
