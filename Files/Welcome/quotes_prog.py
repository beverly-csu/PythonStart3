#напиши здесь свою программу
with open('quotes.txt', 'r', encoding='utf-8') as file:
    print(file.read())

author = input('Введите автора данного отрывка:')
with open('quotes.txt', 'a', encoding='utf-8') as file:
    text = '(' + author + ')\n'
    file.write(text)