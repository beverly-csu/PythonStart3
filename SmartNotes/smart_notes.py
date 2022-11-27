from PyQt5.QtWidgets import (
    QLabel, QPushButton, QApplication, QWidget, QVBoxLayout,
    QHBoxLayout, QListWidget, QTextEdit, QLineEdit
)
import json

# Создание функций
def show_note():
    note_title = list_notes.selectedItems()[0].text()
    note_text = notes[note_title]['text']
    note_field.setText(note_text)


# Создание функций

# Создание приветственного файла
notes = {
    'Первая заметка': {
        'text': 'Ваша первая заметка была создана автоматически!',
        'tags': ['обучение', 'умные заметки']
    }
}

with open('notes.json', 'w', encoding='utf-8') as file:
    json.dump(notes, file)
# Создание приветственного файла

# Основа приложения
app = QApplication([])
window = QWidget()
note_field = QTextEdit()
lbl_note = QLabel('Список заметок:')
list_notes = QListWidget()
btn_create_note = QPushButton('Добавить заметку')
btn_delete_note = QPushButton('Удалить заметку')
btn_save_note = QPushButton('Сохранить заметку')
lbl_tag = QLabel('Список тегов:')
list_tags = QListWidget()
line_tag_search = QLineEdit()
btn_add_tag = QPushButton('Добавить к заметке')
btn_remove_tag = QPushButton('Открепить от заметки')
btn_search_by_tag = QPushButton('Искать заметки по тегу')
# Основа приложения

# Направляющие
main_layout = QHBoxLayout()
left_layout = QVBoxLayout()
right_layout = QVBoxLayout()
h_1 = QHBoxLayout()
h_2 = QHBoxLayout()
h_3 = QHBoxLayout()
h_4 = QHBoxLayout()
h_5 = QHBoxLayout()
h_6 = QHBoxLayout()
h_7 = QHBoxLayout()
h_8 = QHBoxLayout()
h_9 = QHBoxLayout()
# Направляющие

# Установка виджетов на направляющие
h_1.addWidget(lbl_note)
h_2.addWidget(list_notes)
h_3.addWidget(btn_create_note)
h_3.addWidget(btn_delete_note)
h_4.addWidget(btn_save_note)
h_5.addWidget(lbl_tag)
h_6.addWidget(list_tags)
h_7.addWidget(line_tag_search)
h_8.addWidget(btn_add_tag)
h_8.addWidget(btn_remove_tag)
h_9.addWidget(btn_search_by_tag)

right_layout.addLayout(h_1)
right_layout.addLayout(h_2)
right_layout.addLayout(h_3)
right_layout.addLayout(h_4)
right_layout.addLayout(h_5)
right_layout.addLayout(h_6)
right_layout.addLayout(h_7)
right_layout.addLayout(h_8)
right_layout.addLayout(h_9)

left_layout.addWidget(note_field)

main_layout.addLayout(left_layout)
main_layout.addLayout(right_layout)

window.setLayout(main_layout)
# Установка виджетов на направляющие

window.show()
app.exec()