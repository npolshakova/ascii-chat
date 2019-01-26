#!/usr/bin/python3

import socket               # Import socket module
import sys
import termios
import struct
import fcntl

s = socket.socket()         # Create a socket object
host = '127.0.0.1' # Get local machine name
port = 1234                # Reserve a port for your service.

# Setup terminal window size
row = 100
col = 100
# change tty/pty setting
winsize = struct.pack("HHHH", row, col, 0, 0)
fcntl.ioctl(sys.stdin, termios.TIOCSWINSZ, winsize)

# change actual window size
sys.stdout.write("\x1b[8;{rows};{cols}t".format(rows=100, cols=100))

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
      temp = s.recv(10).decode('utf-8')
      sys.stdout.write(temp)
      if temp is None:
         break
   except (KeyboardInterrupt,socket.error):
         s.close                     # Close the socket when done
         s.shutdown(socket.SHUT_RD)
         print('closed')
         break
