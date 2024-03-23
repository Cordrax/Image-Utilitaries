from PIL import Image

def get_image_size(path):
    img = Image.open(path)
    imsize = img.size
    return imsize

def get_image_mode(path):
    img = Image.open(path)
    immode = img.mode
    return immode

def get_image_format(path):
    img = Image.open(path)
    imformat = img.format
    return imformat

def get_image_color(path):
    img = Image.open(path)
    cr = 0
    cg = 0
    cb = 0
    for x in range(img.size[0]):
        for y in range(img.size[1]):
            r, g, b = img.getpixel((x, y))[0], img.getpixel((x, y))[1], img.getpixel((x, y))[2]
            if r > g and r > b:
                cr += 1
            elif g > r and g > b:
                cg += 1
            elif b > r and b > g:
                cb += 1
    
    if cr > cb and cr > cg:
        dominant = "red"
    elif cg > cb and cg > cr:
        dominant = "green"
    elif cb > cg and cb > cr:
        dominant = "blue"
    
    if cr < cg and cr < cb:
        weak = "red"
    elif cg < cr and cg < cb:
        weak = "green"
    elif cb < cg and cb < cr:
        weak = "blue"
    
    if dominant == "red":
        if weak == "blue":
            second = "green"
        else:
            second = "blue"
    elif dominant == "green":
        if weak == "blue":
            second = "red"
        else:
            second = "blue"
    else:
        if weak == "red":
            second = "green"
        else:
            second = "red"
            

            print(dominant)
            return dominant

path = "C:/Users/Martin/Documents/Work/Pgms/ofof.png"

get_image_color(path)
