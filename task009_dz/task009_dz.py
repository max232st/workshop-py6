# Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка,
# стоящих на нечётной позиции. Пример: - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

# def f(numbers):
#     s = 0
#     for i in range(len(numbers)):
#         if i % 2 != 0:
#             odd_numbers.append(numbers[i])
#             s += numbers[i]
#     print(f'Список чисел на нечетных позициях(индексах) -> {odd_numbers}')
#     print(f'Сумма чисел на нечетных позициях равна {s}')

# numbers = [2, 3, 5, 9, 3]
# odd_numbers = []
# print(f'Задан список {numbers}')
# f(numbers)

import random
numbers = [random.randint(3, 12) for i in range(0, 6)]
print(numbers)

result = list(enumerate(numbers))
print(list(result))

def f(numbers):
    s = 0
    for i in range(len(numbers)):
        if i % 2 != 0:
            temp.append(numbers[i])
            s += numbers[i]
    print(f'Список чисел на нечетных позициях(индексах) -> {temp}')
    print(f'Сумма чисел на нечетных позициях равна {s}')

temp = []
print(list(filter(f(numbers), temp)))