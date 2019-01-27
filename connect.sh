#!/bin/sh

# Arg 1 is the ip you are connecting to
# Arg 2 is the port
# Arg 3 is the Webcam Device Number (Try 0 if unsure)
# Arg 4 is the Microphone Device Number (Try 0 or 1 if unsure)

./sender_launch.sh $1 $2 $3 $4

./receiver_launch.sh $1 $2 

