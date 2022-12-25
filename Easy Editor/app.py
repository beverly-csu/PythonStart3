from PyQt5.QtWidgets import (
    QApplication, QWidget, QLabel, QPushButton,
    QListWidget, QVBoxLayout, QHBoxLayout, QFileDialog
)
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
        image_list.clear()
        image_list.addItems(files)


# Function

# Connecting
btn_dir.clicked.connect(showFiles)
# Connecting

# Run
window.show()
app.exec()
# Run