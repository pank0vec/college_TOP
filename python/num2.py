import random

# список случайных чисел

a = [random.randint(-10, 10) for i in range(10)]

print("Исходный список:", a)

# Список четных чисел
chet = []

for i in a:
    if i % 2 == 0:
        chet.append(i)

print("Четные числа:", chet)

# Список нечетных чисел
nechet = []

for i in a:
    if i % 2 != 0:
        nechet.append(i)

print("Нечетные числа:", nechet)

# Список отрицательных чисел
otrav = []

for i in a:
    if i < 0:
        otrav.append(i)

print("Отрицательные числа:", otrav)

# Список положительных чисел
poloj = []

for i in a:
    if i > 0:
        poloj.append(i)

print("Положительные числа:", poloj)
