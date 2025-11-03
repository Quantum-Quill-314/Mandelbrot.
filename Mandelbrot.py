from PIL import Image as img
image_w, image_h = 6500,6500
real_start, real_end = -2.0, 1.0
im_start, im_end = -1.5, 1.5
max_interation = 100
Fractal = img.new('RGB', (image_w, image_h), 'black')


def mandelbrot(c):
    z = 0 + 0j
    for i in range (max_interation):
        z = (z**2) + c
        if (abs(z) > 2):
            return i +1
    else:
        return 0

for y in range(image_h):
    for x in range(image_w):
        im = im_end - (y*(3/image_h))
        c = (real_start + (x*(3/image_w))) + im*1j
        m = mandelbrot(c)
        if (m == 0):
            color = (0,0,0)
        else:
            r = (m*37) % 256
            g = (m*17) % 256
            b = (m*29) % 256
            color = (r,g,b)
        Fractal.putpixel((x,y), color)

Fractal.save("my_fractal.png")

print("Fractal saved!")
