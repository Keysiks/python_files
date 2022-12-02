from PIL import Image, ImageFilter


class Fotoshop:

    def change_year_time(self, name):
        im = Image.open('')
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
