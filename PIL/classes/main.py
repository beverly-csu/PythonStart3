from PIL import Image, ImageFilter

class ImageEditor:
    def __init__(self, filename):
        self.filename = filename
        self.original = None
        self.changed = []

    def open(self):
        try:
            self.original = Image.open(self.filename)
            self.original.show()
        except:
            print('Такого изображения нету :(')

    def do_bw(self):
        if self.original is not None:
            gray = self.original.convert('L')
            self.changed.append(gray)
            old = self.filename.split('.')
            new = old[0] + '_bw.' + old[1]
            gray.save(new)


MyImage = ImageEditor('PIL/classes/cat.jpg')
MyImage.open()
MyImage.do_bw()
for im in MyImage.changed:
    im.show()