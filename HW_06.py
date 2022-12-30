# 1.Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.
# Пример: [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

# import random
# my_list = []
# a = int(input('Введите кол-во элементов в списке: '))
# for i in range(a):
#     my_list.append(random.randint(0,11))
# print(my_list)
# summ = 0
# for i in range(len(my_list)):
#     if i%2==1:
#         summ += my_list[i]
# print(f'Сумма элементов списка, стоящих на нечетных позициях - {summ}')

# Новое решение!

import random
a = int(input('Введите кол-во элементов в списке: '))
my_list = [random.randint(0,10) for i in range(a)]
print(f'Рандомный список - {my_list}')
new_list = [my_list[i] for i in range(len(my_list)) if i%2==1]
print(f'Элементы списка, стоящие на нечетных позициях - {new_list}')
print(f'Сумма элементов - {sum(new_list)}')



# 2.Задайте список из n чисел последовательности (1 + 1/n)^n. Вывестив консоль сам список и сумму его элементов.

# n = int(input('Введите число: '))
# my_list = []
# for i in range(1, n+1):
#     my_list.append((1+1/i)**i)
# print(my_list)
# print(round(sum(my_list), 2))

# Новое решение!

# n = int(input('Введите число: '))
# my_list = [(1+1/i)**i for i in range(1, n+1)]
# print(my_list)
# print(round(sum(my_list), 2))



# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов (Негафибоначчи).
# Пример: для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]

# a = int(input('Введите число: '))
# x = 0
# y = 1
# my_list = [x, y]
# summ = 0
# for i in range(a-1):
#     summ =x+y
#     x = y
#     y = summ
#     my_list.append(summ)
# x = 0
# y = 1
# summ = 0
# my_list.insert(0, 1)
# for i in range(a-1):
#     summ =x+y
#     x = y
#     y = summ
#     if i%2 == 0:
#         summ = - summ
#     my_list.insert(0, summ)
# print(my_list)

# Новое решение!

# a = int(input('Введите число: '))
# x = 0
# y = 1
# my_list = [x, y]
# summ = 0
# for i in range(a-1):
#     summ =x+y
#     x = y
#     y = summ
#     my_list.append(summ)
# li = my_list
# li = list(map(lambda j: -1 * j, li))
# for i in range(1, len(li)):
#     j =  li[i]
#     if i%2 == 0:
#         my_list.insert(0, j)
#     else:
#         my_list.insert(0, -j)
# print(my_list)