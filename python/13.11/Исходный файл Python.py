a = int(input("Введите первое число: "))
b = int(input("Введите второе число: "))

sum_even = 0
sum_odd = 0
sum_9 = 0

count_even = 0
count_odd = 0
count_9 = 0

for i in range(a, b + 1): 
    if i % 2 == 0:
        sum_even += i
        count_even += 1

    if i % 2 != 0: 
        sum_odd += i
        count_odd += 1

    if i % 9 == 0: #кратное
        sum_9 += i
        count_9 += 1

print("Сумма четных:", sum_even)
print("Среднее четных:", sum_even / count_even if count_even else 0)

print("Сумма нечетных:", sum_odd)
print("Среднее нечетных:", sum_odd / count_odd if count_odd else 0)

print("Сумма чисел, кратных 9:", sum_9)
print("Среднее чисел, кратных 9:", sum_9 / count_9 if count_9 else 0)