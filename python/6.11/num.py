import random

numbers = [random.randint(-10, 10) for i in range(10)]

print("Список:", numbers)


#1
negative = sum(x for x in numbers if x < 0)
even = sum(x for x in numbers if x % 2 == 0)
odd = sum(x for x in numbers if x % 2 != 0)

product = 1
for i in range(0, len(numbers), 3):
    product *= numbers[i]

min_in = numbers.index(min(numbers))
max_in = numbers.index(max(numbers))

start = min(min_in, max_in) + 1
end = max(min_in, max_in)

between_product = 1
for x in numbers[start:end]:
    between_product *= x

positive = [i for i in range(len(numbers)) if numbers[i] > 0]

if len(positive) >= 2:
    positive_sum = sum(numbers[positive[0] + 1:positive[-1]])
else:
    positive_sum = 0

print("Сумма отрицательных:", negative)
print("Сумма четных:", even)
print("Сумма нечетных:", odd)
print("Произведение элементов с индексами кратными 3:", product)
print("Произведение между минимумом и максимумом:", between_product)
print("Сумма между первым и последним положительными:", positive_sum)