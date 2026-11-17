
try:
    number = int(input("Введите целое число: "))
    print("Квадрат числа:", number ** 2)

except ValueError:
    print("Введите целое число")
