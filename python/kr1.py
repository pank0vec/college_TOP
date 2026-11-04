"""4. Поиск простых чисел
# Найдите все простые числа в диапазоне от 2 до N

n = 20"""

i = 20

n = 20
for i in range(2, n):
    is_simple = True
    for j in range(2, i):
        if i % j == 0: 
            is_simple = False
    if is_simple:
        print(i, "простое")
    else:
        print(i, "не простое")

#найдите все делители числа N

#12 - 2, 3, 4, 6

n = int(input("number: "))

for i in range(1, n + 1):
    if n % i == 0:
        print(i)

"""8. Поиск совершенных чисел
# Найдите все совершенные числа до N
# Совершенное число равно сумме своих делителей (исключая само число)
n = 10000"""

n = 40000000
for number in range(1, n):
    summa = 0
    for j in range(1, number):
        if number % j == 0:
            summa += j
    if summa == number:
        print(number, "совершенное")