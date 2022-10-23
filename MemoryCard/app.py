from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QLabel, QPushButton, QVBoxLayout, QApplication
from PyQt5.QtWidgets import QWidget, QRadioButton, QHBoxLayout
from PyQt5.QtWidgets import QGroupBox


app = QApplication([])
window = QWidget()

lbl_question = QLabel('Тут будет будующий вопрос)))')
btn_ok = QPushButton('Ответить')
grpbox_answers = QGroupBox('Варианты ответов:')

rbtn_1 = QRadioButton('1')
rbtn_2 = QRadioButton('2')
rbtn_3 = QRadioButton('3')
rbtn_4 = QRadioButton('4')

h_line_ans = QHBoxLayout()
v_line_ans_1, v_line_ans_2 = QVBoxLayout(), QVBoxLayout()

v_line_ans_1.addWidget(rbtn_1)
v_line_ans_1.addWidget(rbtn_2)
v_line_ans_2.addWidget(rbtn_3)
v_line_ans_2.addWidget(rbtn_4)

h_line_ans.addLayout(v_line_ans_1)
h_line_ans.addLayout(v_line_ans_2)
grpbox_answers.setLayout(h_line_ans)

grpbox_result = QGroupBox('Результаты теста')


v_line_main = QVBoxLayout()
h_line_main_1 = QHBoxLayout()
h_line_main_2 = QHBoxLayout()
h_line_main_3 = QHBoxLayout()

h_line_main_1.addWidget(lbl_question, alignment=Qt.AlignCenter)
h_line_main_2.addWidget(grpbox_answers)
h_line_main_3.addStretch(1)
h_line_main_3.addWidget(btn_ok, stretch=3)
h_line_main_3.addStretch(1)

v_line_main.addLayout(h_line_main_1)
v_line_main.addLayout(h_line_main_2)
v_line_main.addLayout(h_line_main_3)

window.setLayout(v_line_main)

window.show()
app.exec()