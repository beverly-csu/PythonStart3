#напиши здесь свою программу
with open('quotes.txt', 'r', encoding='utf-8') as file:
    print(file.read())

author = input('Введите автора данного отрывка:')
with open('quotes.txt', 'a', encoding='utf-8') as file:
    text = '(' + author + ')\n'
    file.write(text)

authors = [author]
choose = input('Хотите ли добавить новую цитату? ')
while choose != 'нет':
    with open('quotes.txt', 'a', encoding='utf-8') as file:
        lyrics = input('Введите цитату: ')
        author = input('Введите автора: ')
        authors.append(author)
        text = lyrics + '\n(' + author + ')\n'
        file.write(text)
    choose = input('Хотите ли добавить новую цитату? ')