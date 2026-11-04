"""5. Анализ последовательности
# Пользователь вводит числа, 0 - конец ввода
# Найдите: количество чисел, их сумму, максимальное и минимальное"""

count = 0
summa = 0
max = None
min = None

while True:
    number = int(input("number: "))

    if max == None:
        max = number
    if min == None:
        min = number

    if number == 0:
        break

    count += 1
    summa += number

    if number > max:
        max = number

    if number < min:
        min = number

print(count, summa, max, min)

