# Напишите программу, удаляющую из текста все слова, содержащие ""абв"".

# string = 'абвгд йцу жзе абв мл млмл мьмддщабв'
# string = string.split()
# result = []
# for i in range(len(string)):
#     if 'абв' not in string[i]:
#         result.append(string[i])
# print(result)


# Создайте программу для игры с конфетами человек против человека.
# Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга. 
# Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет. 
# Все конфеты оппонента достаются сделавшему последний ход. 
# Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?
# a) Добавьте игру против бота
# b) Подумайте как наделить бота ""интеллектом""

# import random
# candy = int(input('Введите количество конфет: '))
# print('Первый ход определяется жеребьевкой')
# first_step = random.randint(0,2)
# if first_step == 0:
#     print('Первым ходит Игрок')
#     while candy > 0:
#         player1 = int(input('Игрок берет конфеты: ')) 
#         candy -= player1
#         print(f'Игрок взял {player1} конфет. Осталось {candy} конфет')
#         if candy == 0:
#             print('Вы выиграли!')
#             break
#         if candy > 28:
#             bot = random.randint(1,28)
#         if candy <=28:
#             bot = candy
#         candy -= bot
#         print(f'Компьютер взял {bot} конфет. Осталось {candy} конфет')
#         if candy == 0:
#             print('Выиграл компьютер!')
#             break
# else: 
#     print('Первым ходит компьютер')
#     while candy > 0:
#         if candy > 28:
#             bot = random.randint(1,28)
#         if candy <=28:
#             bot = candy
#         candy -= bot
#         print(f'Компьютер взял {bot} конфет. Осталось {candy} конфет')
#         if candy == 0:
#             print('Выиграл компьютер!')
#             break
#         player1 = int(input('Игрок берет конфеты: ')) 
#         candy -= player1
#         print(f'Игрок взял {player1} конфет. Осталось {candy} конфет')
#         if candy == 0:
#             print('Вы выиграли!')
#             break



# Создайте программу для игры в ""Крестики-нолики"".

# field = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# print(f'{field[0]} | {field[1]} | {field[2]}')
# print('---------')
# print(f'{field[3]} | {field[4]} | {field[5]}')
# print('---------')
# print(f'{field[6]} | {field[7]} | {field[8]}')
# print()
# step = 0
# res = 0
# turn = int(input('Ходят крестики:'))
# print()
# field[turn-1] = 'X'
# print(f'{field[0]} | {field[1]} | {field[2]}')
# print('---------')
# print(f'{field[3]} | {field[4]} | {field[5]}')
# print('---------')
# print(f'{field[6]} | {field[7]} | {field[8]}')
# print()

# while step < 4:
#     turn = int(input('Ходят нолики:'))
#     print()
#     field[turn-1] = '0'
#     print(f'{field[0]} | {field[1]} | {field[2]}')
#     print('---------')
#     print(f'{field[3]} | {field[4]} | {field[5]}')
#     print('---------')
#     print(f'{field[6]} | {field[7]} | {field[8]}')
#     print()

#     if (field[0]== '0' and field[1] == '0'and field[2]== '0' or
#     field[3]== '0' and field[4]== '0' and field[5] == '0' or
#     field[6] == '0'and field[7]== '0' and field[8] == '0' or
#     field[0] == '0'and field[3]== '0' and field[6]== '0' or
#     field[1] == '0'and field[4] == '0'and field[7]== '0' or
#     field[2] == '0'and field[5] == '0'and field[8]== '0' or
#     field[0] == '0'and field[4]== '0' and field[8]== '0' or
#     field[2] == '0'and field[4]== '0' and field[6] == '0'):
#         res = True
#         print('Выиграли нолики!')
#         break

#     turn = int(input('Ходят крестики:'))
#     print()
#     field[turn-1] = 'X'
#     print(f'{field[0]} | {field[1]} | {field[2]}')
#     print('---------')
#     print(f'{field[3]} | {field[4]} | {field[5]}')
#     print('---------')
#     print(f'{field[6]} | {field[7]} | {field[8]}')
#     print()
   
#     if (field[0]== 'X' and field[1]== 'X' and field[2]== 'X' or
#     field[3]== 'X' and field[4]== 'X' and field[5] == 'X'or
#     field[6]== 'X' and field[7]== 'X' and field[8]== 'X' or
#     field[0]== 'X' and field[3]== 'X' and field[6]== 'X' or
#     field[1]== 'X' and field[4]== 'X' and field[7]== 'X' or
#     field[2]== 'X' and field[5] == 'X'and field[8] == 'X'or
#     field[0] == 'X'and field[4] == 'X'and field[8] == 'X'or
#     field[2] == 'X'and field[4] == 'X'and field[6] == 'X'):
#         res = True
#         print('Выиграли крестики!') 
#         break  
#     step += 1
# if res != True:
#     print('Ничья')
  



# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.

#aaabbbbbccccccc = 3a5b7c


# string = 'aaabbbbbccccccc'
# result = []
# count = 0
# count1 = 0
# count2 = 0
# for i in range(len(string)):
#     if 'a' in string[i]:
#         count+=1  
#     if 'b' in string[i]:
#         count1+=1
#     if 'c' in string[i]:
#         count2+=1
# print(string)
# print(f'{count}a{count1}b{count2}c')

