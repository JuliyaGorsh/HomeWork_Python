# Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.
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


# Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# Пример:
# [2, 3, 4, 5, 6] => [12, 15, 16]
# [2, 3, 5, 6] => [12, 15]

# import random
# my_list = []
# a = int(input('Введите кол-во элементов в списке: '))
# for i in range(a):
#     my_list.append(random.randint(0,11))
# print(my_list)

# new_list = []
# count= 1
# for i in range(a//2):
#     new_list.append(my_list[i] * my_list[len(my_list)-count])
#     count+=1
# if len(my_list)%2==0:
#     print(new_list)
# else:
#     new_list.append((my_list[a//2]**2))
#     print(new_list)


# Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и 
# минимальным значением дробной части элементов. (подробности в конце записи семинара).
# Пример: [1.1, 1.2, 3.1, 5, 10.01] => 0.19

# import random
# my_list1 = []
# new_list1 = []
# a = int(input('Введите кол-во элементов в списке: '))
# for i in range(a):
#     my_list1.append(round(random.uniform(0,11), 2))
# print(my_list1)
# for i in range(len(my_list1)):
#     if my_list1[i]*100%100 > 0:
#         new_list1.append(round(my_list1[i]*100%100))
# print(f'Значения дробных частей - {new_list1}')
# print(f'Максимальная дробная часть - {(max(new_list1))/100}')
# print(f'Минимальная дробная часть - {(min(new_list1))/100}')
# print(f'Разница между значениями дробных частей - {round((max(new_list1) - min(new_list1))/100, 2)}')


# Напишите программу, которая будет преобразовывать десятичное число в двоичное. Без применения встроеных методов (арифметически)
# Пример:
# 45 -> 101101
# 3 -> 11
# 2 -> 10 27 = 11011 19=10011

# a = int(input('Введите десятичное число для преобразования в двоичное: '))
# b =0
# my_list = []
# i=0
# while a >= 1:
#     b = a%2
#     a = a//2
#     my_list.insert(-1-i, b)
#     i+=1
# print(f'Число {a} в двоичной системе: ')
# print(*my_list)


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


