from PIL import Image, ImageTk

def htrgb(hex):
    res = 0
    char = "abcdef"
    list = []
    flist = []
    for d in range(0,6,2):
        res = 0
        for p in range(0,2):
            for k in range(len(char)):
                yes = 0
                res = 0
                if hex[d+p] == char[k]:
                    res += k+10
                    yes = 1
                    break
            if yes == 0:
                res += int(ipt[d+p])
            if p == 0:
                res *= 16
            if res == 16:
                print(res)
            for d in range(0,6,2):
                flist.append(list[d]+list[d+1])
            return flist

pat = input("Enter the path :")
path = ""
for d in range(len(pat)):
    if pat[d] == "\\":
        path += "/"
    else:
        path += pat[d]
im = Image.open(path)
ipt = int(input("How many colors to replace ?"))
ltorep = []
lrep = []
for d in range(ipt):
    ltorep.append(input("The color to replace:"))
for d in range(ipt):
    lrep.append(input("With which colors to replace:"))
for d in range(ipt):
    for x in range(im.size[0]):
        for y in range(im.size[1]):
            if im.getpixel(x, y) == htrgb(ltorep(d)):
                im.putpixel((x, y), (htrgb(lrep[d])))
im.show()
