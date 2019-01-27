#!/bin/sh

# Arg 1 is the ip
# Arg 2 is the port

# Launch the sound sender
cvlc rtp://$1@:$(($2 + 1)) &

sleep 2

# Launch the ASCII Viewer
./receiver_client.py $1 $2

