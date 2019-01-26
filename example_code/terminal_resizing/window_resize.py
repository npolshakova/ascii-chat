#!/usr/bin/python3
import sys
import termios
import struct
import fcntl

nrows = 32
ncols = 100
winsize = struct.pack("HHHH", nrows, ncols, 0, 0)
fcntl.ioctl(sys.stdin, termios.TIOCSWINSZ, winsize)
sys.stdout.write("\x1b[8;{rows};{cols}t".format(rows=nrows, cols=ncols))
