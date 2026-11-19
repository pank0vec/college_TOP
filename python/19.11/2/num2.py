text = input("Введите текст: ")
words = input("Введите слова через пробел: ").split()

for word in words:
    text = text.replace(word, word.upper())

print(text)