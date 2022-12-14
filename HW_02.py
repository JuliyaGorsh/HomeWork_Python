# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
# Пример:
# 6782 -> 23
# 0,56 -> 11

number = input('Введите число: ')
summ = 0
for i in number:
    if i != '.' and i != ',' and i != '-':
        summ += int(i)
print(summ)



# Задайте список из n чисел последовательности (1 + 1/n)^n. Вывестив консоль сам список и сумму его элементов.

# n = int(input('Введите число: '))
# my_list = []
# for i in range(1, n+1):
#     my_list.append((1+1/i)**i)
# print(my_list)
# print(round(sum(my_list), 2))

    
# Реализуйте алгоритм перемешивания списка. Встроенный алгоритм SHUFFLE не использовать! Реализовать свой метод

# import random
# my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# print(f'Начальный список - {my_list}')
# for i in range(len(my_list)):
#     n = random.randint(0, (len(my_list)-1))
#     my_list.append(my_list.pop(n))

# print(f'Перемешанный список - {my_list}')


# ДОПОЛНИТЕЛЬНО, НО НЕОБЯЗАТЕЛЬНО:
# Написать программу, которая состоит 4 из этапов:
# - создает список из рандомных четырех значных чисел
# - принимает с консоли цифру и удаляет ее из всех элементов списка
# - цифры каждого элемента суммирует пока результат не станет однозначным числом
# - из финального списка убирает все дублирующиеся элементы
# - после каждого этапа выводить результат в консоль
# Пример:
# - 1 этап: [2634, 6934, 7286, 3353, 4602, 3176, 3796]
# - 2 этап: Введите цифру: 3
# - 2 этап: [264, 694, 7286, 5, 4602, 176, 796]
# - 3 этап: 264 -> 2+6+4 -> 12 -> 1+2 -> 3
# - 3 этап: [3, 1, 5, 5, 3, 5, 4]
# - 4 этап: [3, 1, 5, 4]


# import random
# my_list = []
# a = int(input('Введите число, определяющее кол-во четырехзначных рандомных чисел:'))
# for i in range(a):
#     my_list.append(random.randint(1000, 9999))
# print(f'{my_list} - рандомный список из {a} чисел')
# my_list1 = []
# n = input('Введите цифру, которую необходимо удалить:')
# my_list = str(my_list)
# for j in my_list:
#     if j != n:
#         my_list1.append(j)
# del my_list1[0]
# del my_list1[len(my_list1) - 1]

# my_list1 = str(my_list1)
# my_list1 = my_list1.replace("'",'')
# my_list1 = my_list1.replace(", ",'')
# my_list1 = my_list1.replace(" ",'')
# print(f'{my_list1} - новый список без цифры {n}') 

# def function(my_list):
#     my_list = str(my_list)
#     summ = 0
#     new_list = []
#     for i in my_list:    
#         if i != '[' and i != ']' and i != "'" and i != ' ' and i != ',': 
#             summ += int(i)
#         elif i == ',':     
#             new_list.append(summ)
#             summ = 0  
#     new_list.append(summ)
#     #print(new_list)
#     return(new_list)

# summ_list =[]
# summ_list = function(my_list1)
# print(f'{summ_list} - сумма цифр')
# summ_list2 = []
# summ_list2 = function(summ_list)
# print(f'{summ_list2} - конечная сумма цифр (до однозначного числа)')

# res = []
# for i in summ_list2:
#     if i not in res:
#         res.append(i)

# print(f'{res} - список без дублирующихся элементов')

