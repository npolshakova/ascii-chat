#!/bin/sh

# Arg 1 is the host
# Arg 2 is the port to host on
# Arg 3 is the Webcam Device Number (Try 0 if unsure)
# Arg 4 is the Microphone Device Number (Try 0 or 1 if unsure)

# Set up the Video Stream
./ascii_webcam_renderer.py $3 | ./sender_server.py $2 &

# Set up the Sound Stream
#FSAMP=16000
#ffmpeg -f alsa -ar $FSAMP -i hw:$4 -ar $FSAMP -ac 1 -f rtp_mpegts rtp://$1:$(($2 + 1))
