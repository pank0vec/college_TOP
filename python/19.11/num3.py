days = ["Понедельник", "Вторник", "Среда", "Четверг",
        "Пятница", "Суббота", "Воскресенье"]

try:
    num = int(input("Введите номер дня (1-7): "))
    print(days[num - 1])

except ValueError:
    print("Введите номер дня")

except IndexError:
    print("Нет такого дня")

finally:
    print("Проверка завершена")