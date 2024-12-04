input = input('Введите слова через запятую, чтобы проверить являются ли они палиндромами: ')
words = [word.strip().lower() for word in input.split(',')]

def is_palindrome():
    global words

    for word in words:
        data = word

        if word == word[::-1]:
            print(f'Слово {word} является палиндромом.')
        else:
            print(f'Слово {word} не является палиндромом.')
is_palindrome()