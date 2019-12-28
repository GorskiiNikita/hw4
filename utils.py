from PIL import Image, ImageFont, ImageDraw
from settings import K_RESIZE


def resize_img(name, in_path, out_path):
    im = Image.open(in_path+name)
    out = im.resize((im.size[0]//K_RESIZE, im.size[1]//K_RESIZE))
    img_format = 'jpeg' if name.split('.')[-1].lower() == 'jpg' else name.split('.')[-1]
    out.save(out_path+name, img_format)


def add_watermark(text, name, in_path, out_path):
    im = Image.open(in_path + name)
    drawing = ImageDraw.Draw(im)

    font = ImageFont.truetype("Pillow/Tests/fonts/FreeMono.ttf", 40)
    width, height = im.size

    for i in range(0, width, width//8):
        for j in range(0, height, height//8):
            drawing.text((i, j), text, font=font)

    img_format = 'jpeg' if name.split('.')[-1].lower() == 'jpg' else name.split('.')[-1]
    im.save(out_path + name, img_format)

