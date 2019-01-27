#!/bin/sh

# Arg 1 is the ip
# Arg 2 is the port

# Launch the ASCII Viewer
./receiver_client.py $1 $2 &

# Launch the sound listener
cvlc rtp://$1@:$2
