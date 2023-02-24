import random

# задаем длину списка
n = int(input("Введите длину списка: "))

# создаем список из n случайных чисел от 1 до 100
lst = [random.randint(1, 100) for i in range(n)]
print("Список:", lst)

# вводим искомое число
x = int(input("Введите искомое число: "))

# находим количество вхождений x в список
count = lst.count(x)
if count > 0:
    print("Число", x, "встречается в списке", count, "раз(а)")
else:
    # находим ближайшее к x число в списке
    closest = min(lst, key=lambda y: abs(x-y))
    print("Число", x, "отсутствует в списке. Ближайшее число:", closest)