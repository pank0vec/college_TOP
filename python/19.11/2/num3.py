text = input("Введите текст: ")

count = text.count(".") + text.count("!") + text.count("?")

print("Количество предложений:", count)