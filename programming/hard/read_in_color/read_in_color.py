from PIL import Image

# use python3 read_in_color.py(in windows, you should pip install Pillow;
# in kali linux, PIL module has already been installed)

img = Image.open("color_img.png")
width = img.width
height = img.height

#print(width)
#print(height)

pixels = []
for i in range(0, width):
    for j in range(0, height):
        pixel = img.getpixel((i, j))
        if pixel not in pixels:           # remove duplicated RGB 
            pixels.append(pixel)
print(pixels)

flag = ""
for pixel in pixels:
    for color in pixel:
        flag += chr(color)

print(flag)
