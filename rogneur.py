from PIL import Image, ImageTk

def rogneur(path):
    im = Image.open(path)
    imf = Image.new("RGB", (512, 512))
    for x in range(im.size):
    for x in range(imf.size[0]):
        for y in range(imf.size[1]):
            if x >= im.size[0] or y >= im.size[1]:
                imf.putpixel((x, y), (255, 255, 255))
            else:
                imf.putpixel((x, y), (im.getpixel((x, y))))
    imf.save("C:/Users/Martin/Documents/Work/Ibrahim/APK/ERBrognbe.png")

rogneur("C:/Users/Martin/Documents/Work/Ibrahim/APK/ERD_Logo_white_background.png")

