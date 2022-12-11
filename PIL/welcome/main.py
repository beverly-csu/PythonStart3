from PIL import Image, ImageFilter


def print_property(img):
    print('Размер:', img.size)
    print('Формат:', img.format)
    print('Тип:', img.mode)


with Image.open('PIL/welcome/cat.jpg') as original:
    print_property(original)
    original.show()

    gray = original.convert('L')
    gray.save('PIL/welcome/cat_gray.jpg')
    gray.show()

    blur = original.filter(ImageFilter.BLUR)
    blur.save('PIL/welcome/cat_blur.jpg')
    blur.show()

    up = original.transpose(Image.ROTATE_180)
    up.save('PIL/welcome/cat_up.jpg')
    up.show()