from PIL import Image

c = 0
c2 = 0
style = ""
print("Enter the picture's path")
img = input()
while c == 0:
    print("Average value or specific values ?(A/S)")
    ipt = input().lower()
    if ipt == "a" or ipt == "average" or ipt == "medium" or ipt == "moyenne":
        print("Minimum or maximum ?")
        ipt2 = input().lower()
        if ipt2 == "minimum" or ipt2 == "min":
            style = "min"
            while c2 == 0:
                print("Enter the minimum average value to keep the pixel")
                min = int(input())
                if min >= 0 and min <= 255:
                    c = 1
                    c2 = 1
                else :
                    print("The minimum value must be between 0 and 255 and an integer")
        elif ipt2 == "max" or ipt2 == "maximum":
            style = "max"
            while c2 == 0:
                print("Enter the minimum average value to keep the pixel")
                max = int(input())
                if max >= 0 and max <= 255:
                    c = 1
                    c2 = 1
                else :
                    print("The maximum value must be between 0 and 255 and an integer")
    elif ipt == "s" or ipt == "specific":
        style = "specific"
        while c2 == 0:
            print("Red value :")
            r = int(input())
            if r >= 0 and r <= 255:
                c2 = 1
            else :
                print("The red value must be between 0 and 255 and an integer")
        c3 = 0
        while c3 == 0:
            print("Green value :")
            g = int(input())
            if g >= 0 and g <= 255:
                c3 = 1
            else:
                print("The green value must be between 0 and 255 and an integer")
        c4 = 0
        while c4 == 0:
            print("Blue value :")
            b = int(input())
            if b >= 0 and b <= 255:
                c4 = 1
                c = 1
            else :
                print("The blue value must be between 0 and 255 and an integer")

    else :
        print("Please do a good answer")

im = Image.open(img)
width, height = im.size

for x in range(0, width):
    for y in range(0, height):
        pr, pg, pb = im.getpixel((x, y))[0], im.getpixel((x, y))[1], im.getpixel((x, y))[2]
        if style == "min":
            if (pr+pg+pb)/3 <= min:
                im.putpixel((x, y), (0, 0, 0, 0))
        elif style == "max":
            if (pr+pg+pb)/3 >= max:
                im.putpixel((x, y), (0, 0, 0, 0))
        elif style == "specific":
            if pr >= r-5 and pr <= r+5 and pg >= g-5 and pg <= g+5 and pb >= b-5 and pb <= b+5:
                im.putpixel((x, y), (0, 0, 0, 0))

print("Show the results ?")
sho = input().lower()
if sho == "y" or sho == "yes":
    im.show()
print("Save the picture?")
sav = input().lower()
if sav == "y" or sav == "yes":
    im.save(img[0:-4]+"-removed"+img[-4:len(img)])
