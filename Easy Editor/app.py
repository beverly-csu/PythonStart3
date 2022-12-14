from PyQt5.QtWidgets import (
    QApplication, QWidget, QLabel, QPushButton,
    QListWidget, QVBoxLayout, QHBoxLayout, QFileDialog
)
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap
from PIL import Image, ImageFilter
import os

# Widgets
app = QApplication([])
window = QWidget()
btn_dir = QPushButton('Open dir')
btn_left = QPushButton('Rotate left')
btn_right = QPushButton('Rotate right')
btn_mirror = QPushButton('Mirror')
btn_sharp = QPushButton('Sharp')
btn_bw = QPushButton('Black&White')
image = QLabel('Image')
image_list = QListWidget()
# Widgets

# Layout's
h_main = QHBoxLayout()
h_btn = QHBoxLayout()
v_left = QVBoxLayout()
v_right = QVBoxLayout()

h_btn.addWidget(btn_left)
h_btn.addWidget(btn_right)
h_btn.addWidget(btn_mirror)
h_btn.addWidget(btn_sharp)
h_btn.addWidget(btn_bw)

v_left.addWidget(btn_dir)
v_left.addWidget(image_list)

v_right.addWidget(image)
v_right.addLayout(h_btn)

h_main.addLayout(v_left, stretch=2)
h_main.addLayout(v_right, stretch=6)
# Layout's

# Options
window.setWindowTitle('EasyEditor')
window.resize(900, 500)
window.setLayout(h_main)
# Options

# Function
curDir = ''
def getDir():
    path = QFileDialog.getExistingDirectory()
    return path

def showFiles():
    path = getDir()
    if len(path) > 0:
        global curDir
        curDir = path
        files = os.listdir(path)
        extensions = ['.png', '.jpg', '.jpeg', '.svg', '.eps', '.bmp']
        images = filter(files, extensions)
        image_list.clear()
        image_list.addItems(images)

def filter(files, extensions):
    images = []
    for file in files:
        for ext in extensions:
            if file.endswith(ext):
                images.append(file)
    return images

class ImageProcessor:
    def __init__(self):
        self.dir = None
        self.filename = None
        self.image = None
        self.save_dir = 'Modifed'

    def loadImage(self, dir, filename):
        self.dir = dir
        self.filename = filename
        img_path = os.path.join(dir, filename)
        self.image = Image.open(img_path)

    def do_bw(self):
       self.image = self.image.convert("L")
       self.saveImage()
       image_path = os.path.join(self.dir, self.save_dir, self.filename)
       self.showImage(image_path)
 
    def saveImage(self):
       path = os.path.join(self.dir, self.save_dir)
       if not(os.path.exists(path) or os.path.isdir(path)):
           os.mkdir(path)
       image_path = os.path.join(path, self.filename)
       self.image.save(image_path)
    
    def showImage(self, path):
        image.hide()
        pixmap = QPixmap(path)
        w, h = image.width(), image.height()
        pixmap = pixmap.scaled(w, h, Qt.KeepAspectRatio)
        image.setPixmap(pixmap)
        image.show()

    def do_flip(self):
        self.image = self.image.transpose(Image.Transpose.FLIP_LEFT_RIGHT)
        self.saveImage()
        image_path = os.path.join(self.dir, self.save_dir, self.filename)
        self.showImage(image_path)

    def do_left(self):
        self.image = self.image.transpose(Image.Transpose.ROTATE_90)
        self.saveImage()
        image_path = os.path.join(self.dir, self.save_dir, self.filename)
        self.showImage(image_path)

    def do_right(self):
        self.image = self.image.transpose(Image.Transpose.ROTATE_270)
        self.saveImage()
        image_path = os.path.join(self.dir, self.save_dir, self.filename)
        self.showImage(image_path)

    def do_sharp(self):
        self.image = self.image.filter(ImageFilter.SHARPEN)
        self.saveImage()
        image_path = os.path.join(self.dir, self.save_dir, self.filename)
        self.showImage(image_path)

imgProc = ImageProcessor()

def showCurrentImage():
    if image_list.currentRow() > 0:
        filename = image_list.currentItem().text()
        imgProc.loadImage(curDir, filename)
        img_path = os.path.join(curDir, filename)
        imgProc.showImage(img_path)
# Function

# Connecting
btn_dir.clicked.connect(showFiles)
btn_mirror.clicked.connect(imgProc.do_flip)
btn_left.clicked.connect(imgProc.do_left)
btn_right.clicked.connect(imgProc.do_right)
btn_sharp.clicked.connect(imgProc.do_sharp)
btn_bw.clicked.connect(imgProc.do_bw)
image_list.currentRowChanged.connect(showCurrentImage)
# Connecting

# Run
window.show()
app.exec()
# Run