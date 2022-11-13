#напиши здесь свою программу
class Pupil:
    def __init__(self, surname, name, mark):
        self.surname = surname
        self.name = name
        self.mark = mark

pupils = []

with open('pupils_txt.txt', 'r', encoding='utf-8') as file:
    for line in file:
        data = line.split(' ')
        pupil = Pupil(data[0], data[1], int(data[2]))
        pupils.append(pupil)
        print(data[0], data[1], '-', int(data[2]))

