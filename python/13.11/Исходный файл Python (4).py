итог = 0
макс = None
мин = None

while True:
    number = int(input("Введите число: "))

    if number == 7:
        print("Good bye!")
        break

    итог += number

    if макс is None or number > макс:
        макс = number

    if мин is None or number < макс:
        мин = number

print("Сумма:", итог)