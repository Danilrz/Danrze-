#Разинков Даниил Николаевич Группа 44-22-114 Вариант 19 Задание 1
import math

def calculate_value(x):
    if x < 1:
        return math.sin(x + x ** 2)
    else:
        return x * math.sqrt(x + 0.3)

try:
    x = float(input("Введите значение x: "))
    result = calculate_value(x)
    print("Результат:", result)
except ValueError:
    print("Ошибка ввода числа")
except Exception as e:
    print("Ошибка:", e)