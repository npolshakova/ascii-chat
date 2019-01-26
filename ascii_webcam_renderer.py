#!/usr/bin/python3

from PIL import Image
import cv2
import sys


def main():
    cam_id = int(sys.argv[1])
    if len(sys.argv) == 3:
        width = int(sys.argv[2])
        height = int(sys.argv[3])
    else:
        width = 600
        height = 450

    capture = cv2.VideoCapture(cam_id)
    while(True):
        ret, cv_image = capture.read()

        cv_image = cv2.cvtColor(cv_image, cv2.COLOR_BGR2RGB)
        image = Image.fromarray(cv_image)

        image.convert(mode="P", matrix=None, dither=Image.FLOYDSTEINBERG, palette=Image.WEB, colors=256)
        pixels = image.load()

        color = 'MNHQ$OC?7>!;:-. '
        color = list(reversed(color))
        out_str = ""
        for ix in range(height):
            if ix % 2 == 0 and ix % 4 == 0:
                for jx in range(width):
                    rgba = pixels[jx, ix]
                    rgb = rgba[:3]
                    out_str += color[int(sum(rgb) / 3.0 / 256.0 * 16.0)]

                out_str += '\n'

        sys.stdout.write(out_str)
        sys.stdout.flush()

    capture.release()

if __name__ == '__main__':
    main()
