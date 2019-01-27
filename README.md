# ascii-chat

`ascii-chat` allows you to videochat from terminal. Tested on Ubuntu 18.04 with the default
gnome-terminal. The code would probably require some minor tweaks to get working on Mac, but there's
no fundamental reason the code is incompatible. 

# Installation

`ascii-chat` requires installation of several other packages, but luckily all of them can be
installed with apt-get. Python OpenCV is used to grab images from the camera (which seems a little
overkill, but it ends up working well...), ffmpeg is used for audio capture and streaming, vlc is
used for audio playing, and xdotool is used for automatic zoom adjustments.

The following command should install all of the necessary dependencies, but it hasn't been tested:

```
apt-get install python3-opencv ffmpeg vlc xdotool
```

# Running

To get a quick taste of ascii-rendered goodness, you can try out `ascii_webcam_renderer.py` which
displays video from your webcam rendered as ascii. You need to provide the webcam device id, which
is probably 0, e.g.

```
./ascii_webcam_renderer.py 0
```

`connect.sh` is the entry point for the video chat software. It requires arguments specifying the
peer's IP Address, and the hardware device numbers for the microphone and webcam. e.g.
```
./connect.sh 192.168.1.123 1234 0 0
```

Each peer should run the connect script (with the appropriate IP addresses and the correct hardware
id for each computer). After launching the script, you will notice the terminal zooms out after 2
seconds. Once both peers are at this step, each peer must press "Enter" to commence the videochat
(this synchronization step is required because the current architecture involves each peer running a
server for one direction of data transmission, and so we must wait for the peer's server to be
running before we connect)

# Architecture

`ascii-chat` is fun because the architecture is amazingly simple and modular. All of the
image-to-ascii mapping happens in `ascii_webcam_renderer.py`. This python script writes the
ascii-rendered webcam stream to stdout. 

The pair of programs `sender_server.py` and `receiver_client.py` provide a simple, portable way to
send data over a network. The sender reads data from stdin, and sends it to the designated host:port
address. The receiver reads all data from its specified port, and prints to stdout. 

The audio sending is handled by ffmpeg. ffmpeg can record from the system microphone and send
directly to a remote udp or rtp port. On the receiver side of the audio, vlc (really cvlc, the
commandline-only version of vlc) connects listens to the rtp port and plays whatever it receives on
that port. All of the audio processing is done in only 2 commands, one in `sender_launch.sh` and one
in `receiver_launch.sh` 

# Future Additions

It would be very easy to add ascii-rendered video streaming to this project. I hope to do so, as it
would only require changing a few lines in `ascii_webcam_renderer.py` to read from a video file
instead of the webcam. 

The audio lags quite a bit (~1-2) seconds, and it would be nice to fix that unfortunately that seems
to be a limitation of ffmpeg streaming, so reducing audio latency may require a more sophisticated
streaming method. It might be worth delaying the video stream to match the audio instead of speeding
up the audio. 

Another fun extension would be to send live speech-to-text transcription of the audio, so that the
conversation could be rendered in ascii as well :)

# Maintainers

Comments or questions welcome at aray.york (at) gmail (dot) com
