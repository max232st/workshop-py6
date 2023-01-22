# Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся
# элементов исходной последовательности.

# import random
# rnd_numbers = [random.randint(3, 17) for i in range(0, 15)]
# # import random
# # rnd_numbers = []
# # for i in range(0, 15):
# #     rnd_numbers.append(random.randint(5, 17))
# print(f'Последовательность случайных чисел: {rnd_numbers}')
# def unique_numbers(rnd_numbers):
#     unique_num = []
#     unique_numbers = set(rnd_numbers)
#     for number in unique_numbers:
#         unique_num.append(number)
#     return unique_num
# print(f'Последовательность неповторяющихся чисел: {unique_numbers(rnd_numbers)}')


import random

rnd_numbers = [random.randint(3, 15) for i in range(0, 10)]
print(rnd_numbers)

unique_num = set(rnd_numbers)
num = [i for i in unique_num if i in unique_num]
print(num)
