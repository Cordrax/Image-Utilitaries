from PIL import Image, ImageTk

def getcolors(pat):
    path = ""
    for d in range(len(pat)):
        if pat[d] == "\\":
            path += "/"
        else:
            path += pat[d]
    im = Image.open(path)
    lcol = []
    for x in range(im.size[0]):
        for y in range(im.size[1]):
            c = 0
            for d in range(len(lcol)):
                if lcol[d] == im.getpixel((x, y)):
                    c = 1
            if c != 1:
                lcol.append(im.getpixel((x, y)))
    return lcol

print(getcolors("C:/Users/Martin/Documents/Programmation/Python/Logo.png"))
