from PIL import Image, ImageFilter


def image_filter():
    im = Image.open('для фотошопа.jpg')
    im = im.filter(ImageFilter.BLUR)
    im = im.filter(ImageFilter.SHARPEN)
    x, y = im.size
    pixels = im.load()
    for i in range(x):
        for j in range(y):
            r, g, b = pixels[i, j]
            pixels[i, j] = r + 5, g + 5, b + 5
    for i in range(x):
        for j in range(y):
            r, g, b = pixels[i, j]
            pixels[i, j] = 255 - r, 255 - g, 255 - b
    im.save('res.png', 'PNG')


# моя программа размывает высветленное, более резкое изображение, затем меняет цвет на 255 - цвет3
# можно сказать меняет сезон года)
image_filter()
