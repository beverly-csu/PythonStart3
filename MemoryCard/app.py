from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QLabel, QPushButton, QVBoxLayout, QApplication
from PyQt5.QtWidgets import QWidget, QRadioButton, QHBoxLayout
from PyQt5.QtWidgets import QGroupBox, QButtonGroup
from random import shuffle


# Свои классы
class Question:
    def __init__(self, question, right_answer, wrong1, wrong2, wrong3):
        self.question = question
        self.right_answer = right_answer
        self.wrong1 = wrong1
        self.wrong2 = wrong2
        self.wrong3 = wrong3
# Свои классы

# Список с вопросами
question_list = [
    Question('Вопрос №1', '2005', '2009', '2012', '2001'),
    Question('Вопрос №2', '1905', '1912', '1967', '1932'),
    Question('Вопрос №3', '988', '968', '1292', '1349'),
    Question('Кто создал Python?', 'Гвидо Ван Россум', 'Билл Гейтс', 'Марк Цукенберг', 'Стив Джобс')
]
# Список с вопросами

# Функции
def show_result():
    grpbox_answers.hide()
    grpbox_result.show()
    btn_ok.setText('Следующий вопрос')

def show_question():
    btn_group.setExclusive(False)
    rbtn_1.setChecked(False)
    rbtn_2.setChecked(False)
    rbtn_3.setChecked(False)
    rbtn_4.setChecked(False)
    btn_group.setExclusive(True)
    grpbox_answers.show()
    grpbox_result.hide()
    btn_ok.setText('Ответить')

def ask(q):
    shuffle(answers)
    lbl_question.setText(q.question)
    answers[0].setText(q.right_answer)
    answers[1].setText(q.wrong1)
    answers[2].setText(q.wrong2)
    answers[3].setText(q.wrong3)
    show_question()

def results():
    if answers[0].isChecked():
        lbl_result.setText('Вы ответили правильно! Поздравляем!')
    else:
        lbl_result.setText('Вы ответили неверно!\nПравильный ответ: ' + answers[0].text())
    show_result()

def start_test():
    global q_index
    if btn_ok.text() == 'Ответить':
        results()
    else:
        ask(question_list[q_index])
        q_index += 1
# Функции

app = QApplication([])
window = QWidget()
q_index = 1

lbl_question = QLabel('Тут будет будующий вопрос)))')
btn_ok = QPushButton('Ответить')

# Создание GroupBox'a с вариантами ответов
grpbox_answers = QGroupBox('Варианты ответов:')
btn_group = QButtonGroup()
rbtn_1 = QRadioButton('1')
rbtn_2 = QRadioButton('2')
rbtn_3 = QRadioButton('3')
rbtn_4 = QRadioButton('4')
btn_group.addButton(rbtn_1)
btn_group.addButton(rbtn_2)
btn_group.addButton(rbtn_3)
btn_group.addButton(rbtn_4)
answers = [rbtn_1, rbtn_2, rbtn_3, rbtn_4]
# Создание GroupBox'a с вариантами ответов

# Создание GroupBox'a с результатом
grpbox_result = QGroupBox('Результаты теста')
lbl_result = QLabel('Правильный ответ: 123')
v_line_result = QVBoxLayout()
v_line_result.addWidget(lbl_result)
grpbox_result.setLayout(v_line_result)
grpbox_result.hide()
# Создание GroupBox'a с результатом

btn_ok.clicked.connect(start_test)

# Создание и установки layout'ов
h_line_ans = QHBoxLayout()
v_line_ans_1, v_line_ans_2 = QVBoxLayout(), QVBoxLayout()

v_line_ans_1.addWidget(rbtn_1)
v_line_ans_1.addWidget(rbtn_2)
v_line_ans_2.addWidget(rbtn_3)
v_line_ans_2.addWidget(rbtn_4)

h_line_ans.addLayout(v_line_ans_1)
h_line_ans.addLayout(v_line_ans_2)
grpbox_answers.setLayout(h_line_ans)

v_line_main = QVBoxLayout()
h_line_main_1 = QHBoxLayout()
h_line_main_2 = QHBoxLayout()
h_line_main_3 = QHBoxLayout()

h_line_main_1.addWidget(lbl_question, alignment=Qt.AlignCenter)
h_line_main_2.addWidget(grpbox_answers)
h_line_main_2.addWidget(grpbox_result)
h_line_main_3.addStretch(1)
h_line_main_3.addWidget(btn_ok, stretch=3)
h_line_main_3.addStretch(1)

v_line_main.addLayout(h_line_main_1)
v_line_main.addLayout(h_line_main_2)
v_line_main.addLayout(h_line_main_3)

window.setLayout(v_line_main)
# Создание и установки layout'ов

ask(question_list[0])

window.show()
app.exec()