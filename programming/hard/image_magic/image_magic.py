from PIL import Image

# use python3 image_magic.py, because PIL module is included by python3

img = Image.open("out_copy.jpg")

size = img.size
width = img.width
height = img.height                             # 1
width_origin = 304
height_origin = width // width_origin           # 92
mode = img.mode
form = img.format

#print(size)
#print(width_origin)
#print(height_origin)

img_back = Image.new(mode, (width_origin, height_origin))
for k in range(0, width):
    i = k // height_origin
    j = k % height_origin
    pixel = img.getpixel((k,0))
    img_back.putpixel((i,j), pixel)

img_back.save("flag.jpg", form)
img_back.show()         # if show() won't display the picture, sudo apt-get install imagemagick
