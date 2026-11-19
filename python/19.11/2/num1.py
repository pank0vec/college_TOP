text = input("Введите строку: ").lower().replace(" ", "")

if text == text[::-1]:
    print("Это палиндром")
else:
    print("Это не палиндром")