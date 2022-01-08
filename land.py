from PIL import Image


def land(land_):
    im = Image.open(land_)
    pixels = im.load()
    x, y = im.size
    r_, g_, b_ = 0, 0, 0
    t = 0
    for i in range(x):
        for j in range(y):
            t += 1
            r, g, b = pixels[i, j]
            r_ += r
            g_ += g
            b_ += b
    print(r_ // t, g_ // t, b_ // t)
    return r_ // t, g_ // t, b_ // t
