ffmpeg -f alsa -ar 44100 -i hw:0 -acodec ac3_fixed -f mpegts udp://127.0.0.1:9999?pkt_size=1316

