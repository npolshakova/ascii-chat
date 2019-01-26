#!/usr/bin/python3
import argparse
from PIL import Image
import sys

parser = argparse.ArgumentParser('Convert an image to ascii')
parser.add_argument('path', help='Path to image for conversion')


def main():
    args = parser.parse_args()

    img = Image.open(args.path)
    if img.mode != "RGB":
        img = img.convert("RGB")
    img.convert(mode="P", matrix=None,dither=Image.FLOYDSTEINBERG, palette=Image.WEB, colors=256)
    img.show()

    width, height = img.size

    pixel = img.load()

    color = "MNHQ$OC?7>!:-;. "
    str = ""
    for i in range(height):
        if i % 2 == 0 and i % 4 == 0:
            for j in range(width):
                rgba = pixel[j,i]
                rgb = rgba[:3]
                str += color[int(sum(rgb) / 3.0 / 256.0 * 16.0)]

            str += "\n"

    sys.stdout.write(str)
    sys.stdout.flush()

if __name__ == '__main__':
    main()
