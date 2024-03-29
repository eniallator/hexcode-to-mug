from sys import argv
import os
from PIL import Image, ImageFont, ImageDraw, ImageColor

output_dimensions = (1612, 640)
font_size = 78
padding = {"top": -14, "right": 3, "bottom": 5}
output_dir = os.path.join(os.getcwd(), "output")

if os.path.isfile(output_dir):
    raise Exception("Specified output directory is a file")
elif not os.path.isdir(output_dir):
    os.mkdir(output_dir)

try:
    arg = argv[1]
except IndexError as e:
    raise Exception("No hexcode argument received")

try:
    int(arg, base=16)
except ValueError:
    raise Exception("Only accepts hex digits for the colour code")

original_code = arg.upper()

if len(arg) == 3:
    hex_list = map(lambda d: d * 2, arg)
    hexcode = "#" + "".join(hex_list)
elif len(arg) == 6:
    hexcode = "#" + arg.upper()
else:
    raise Exception("Colour has to be either 3 or 6 hex digits long")

image = Image.new("RGB", output_dimensions, color=ImageColor.getrgb(hexcode))

font = ImageFont.truetype("NotoSans-CondensedBold.ttf", font_size)
draw = ImageDraw.Draw(image)

hex_str = "#" + original_code
hexcode_text_size = font.getsize(hex_str)

draw.rectangle(
    (
        (0, output_dimensions[1] - hexcode_text_size[1] - padding["top"]),
        (output_dimensions[0], output_dimensions[1]),
    ),
    fill=(255, 255, 255),
)

draw.text(
    (
        output_dimensions[0] - hexcode_text_size[0] - padding["right"],
        output_dimensions[1] - hexcode_text_size[1] - padding["bottom"],
    ),
    hex_str,
    font=font,
    fill=0,
)

image.save(os.path.join(output_dir, f"{hex_str[1:]}.png"))
