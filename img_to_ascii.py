from PIL import Image
import sys

img = Image.open("test.jpg")
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
