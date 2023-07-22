# Дан массив, состоящий из целых чисел. Напишите программу, которая в данном массиве
# определит количество элементов, у которых два соседних и, при этом, оба соседних
# элемента меньше данного. Сначала вводится число N — количество элементов в массиве
# Далее записаны N чисел — элементы массива. Массив состоит из целых чисел.

# from random import randint

# array = []
# count = 0
# n = int(input("введите величину массива : "))
# for i in range(1, n+1):
#     array.append(randint(1, 25))
# print(array)
# #создал рандомно заполняемый массив

# for i in range(1, len(array)-1):
#     if array[i-1] < array[i] > array[i+1]:
#         count += 1
# print(count)
#



# Дан список чисел. Посчитайте, сколько в нем пар элементов, равных друг другу.
#  Считается, что любые два элемента, равные друг другу образуют одну пару, которую необходимо посчитать.
# Вводится список чисел. Все числа списка находятся на разных строках.


# from random import randint

# def filling(p):
#     list=[]
#     for i in range(p):
#         list.append(randint(0, 15))
#     return list


# array = []
# count = 0
# n = int(input("введите величину массива : "))
# for i in range(1, n):
#     array.append(randint(1, 10))
# print(array)
# #создал рандомно заполняемый массив

# # list1 = list(array)
# # # ииз массива перевел в список.
# # mno = set(list1)
# # из списка создал множество . только план был очень плохим.

#РЕШЕНИЕ из чата и семинара

# from collections import Counter
# from random import randint

# array = []
# count = 0
# n = int(input("введите величину массива : "))
# for i in range(1, n):
#     array.append(randint(1, 10))
# print(array)
# #создал рандомно заполняемый массив

# dictionary = Counter(array)
# for key, values in dictionary.items():
#     if int(values)//2:
#         print(f'{key} , количество пар: {int(values)//2}')


# РЕШЕНИЕ ОТ ПРЕПОДА
# import random

# size = int(input("введите размер списка : "))
# my_list = [random.randint(0,10) for _ in range(size)]
# print(my_list)
# count = 0
# i = 0
# while i < len(my_list):
#     j = i + 1
#     while j < len(my_list):
#         if my_list[i] == my_list[j]:
#             print(my_list[i], my_list[j])
#             my_list.pop(j)
#             my_list.pop(i)
#             count += 1
#             i=0
#             j=0
#         j += 1
#     i += 1
# print(my_list)



# Задача 30: Заполните массив элементами арифметической прогрессии. Её первый элемент,
# разность и количество элементов нужно ввести с клавиатуры. Формула для получения n-го
# члена прогрессии: an = a1 + (n-1) * d.
# Каждое число вводится с новой строки.

# a1 = int(input("первый элемент "))
# d = int(input("шаг"))
# n = int(input( "количество"))
# for i in range(n):
#     print(a1+i*d)



# Задача 32: Определить индексы элементов массива (списка),
# значения которых принадлежат заданному диапазону (т.е. не меньше заданного
# минимума и не больше заданного максимума)

# Ввод: [-5, 9, 0, 3, -1, -2, 1, 4, -2, 10, 2, 0, -9, 8, 10, -9, 0, -5, -5, 7]
# Вывод: [1, 9, 13, 14, 19]

# list1 = [-5, 9, 0, 3, -1, -2, 1, 4, -2, 10, 2, 0, -9, 8, 10, -9, 0, -5, -5, 7]
# min_number = int(input('min : '))
# max_number = int(input('max : '))
# for i in range(len(list1)):
#     if list1[i] >= min_number and list1[i] <= max_number:
#         print(i)


########################################################################################
########################################################################################

# dict1 = {"first": 1, "second": 2, "third": 3}     # создаем словарь

# for keys, value in dict1.items():
#     print(keys, value)                                   # вывод ключа и значения

# print(dict1.items())                                # вывод списка [], внутри картежи из нашего словаря

# for i in dict1.items():
#     print(i)                                    # вывод картежей.


# dict1 = {"first": 1, "second": 2, "third": 3}
# print(dict1)
# dict1["four"] = 4                               # добавили 4й элемент в наш список
# print(dict1)
# dict1.update({"four": 4, "five": 5})                               # добавили НЕСКОЛЬКО  элементов в наш список
# print(dict1)
# print(dict1["second"])               # обратились к словарю и получили элемент (если элемента нет - выводит ошибку)
# print(dict1.get("second"))   # обратились к словарю и получили элемент (если элемента нет - выводит NONE . и программа не останавливается )
# print(dict1.get("four", 0)) #если нет такого элемента - выведет то что мы написали . тоесть 0 .
# print(dict1.get("second", 0)) #если элемент есть - выведет - значение ключа . а 0 будет игнорировать

# print(dict1)
# dict1.pop("second")     #удаление элемента из списка
# print(dict1)

# print(dict1.keys())     #выводит только ключи
# print(dict1.values())   #выводит только значения


# Вложенные списки

# dict2 = {"Tom": {"English": 5, "Math": 5 }, "Red": {"English": 4, "Math": 4 }}
# print(dict2)
# for i in dict2["Tom"].items():
# #функция айтимс - переводит в картежи
#     print(*i)
# #ставим звездочку для красивого вывода картежей

# # print(dict2["Red"]["Math"])
# # # обращаемся точечно . к оценку по конкретному предмету по конкретному ученику.

# dict2.update({'Wer': {"English": 3, "Math": 3 }})
# #добавили в список ученика с оценками
# print(dict2)

# dict2['Tom'].update({'Trud': 6})
# print(dict2)
# добавили новый предмет в список "ТОМ"

# dict2["Red"]["Math"] = 15
# print(dict2)
# # Изменили оценку

# t = "Red"
# dict2[t]["Math"] = 15
# print(dict2)
# # можно и переменную вставлять.


# Рекурсия

# Последовательностью Фибоначчи называется последовательность чисел a0, a1, ..., an, ..., где
# a0 = 0, a1 = 1, ak = ak-1 + ak-2 (k > 1).
# Требуется найти N-е число Фибоначчи
# Input: 7
# Output: 13

# Задание необходимо решать через рекурсию

# def fibo(x):
#     if x in [1, 2]:
#         return 1
#     return fibo(x-1) + fibo(x-2)

# n = int(input("go : "))
# list1 = []
# for i in range(1, n):
#     list1.append(fibo(i))
# list1.insert(0, 0)
# print(list1)


# def f(n):
#     if n == 0 or n == 1:
#         return n
#     return f(n-1) + f(n-2)

# print(f(int(input("go : "))))


# 33.Хакер Василий получил доступ к классному журналу
# и хочет заменить все свои минимальные оценки на максимальные.
# Напишите программу, которая заменяет оценки Василия,
# но наоборот: все максимальные – на минимальные.

# Input: 5 -> 1 3 3 3 4
# Output: 1 3 3 3 1

# n = int(input("go : "))
# array = list()
# for i in range(n):
#     array.append(int(input("array -----   : ")))
# print(*array)

# array = [int(input("оценка: ")) for i in range(int(input("введите количество оценок : ")))]
# print(*array)

# maxNumber = max(array)
# minNumber = min(array)

# for i in range(len(array)):
#     if array[i] == maxNumber:
#         array[i] = minNumber
# print(*array)


# 35.Напишите функцию, которая принимает одно число и проверяет, является ли оно простым
# Напоминание: Простое число - это число, которое имеет 2 делителя: 1 и n(само число)

# Input: 5
# Output: yes


# def prost(x):
#     i = 2
#     flag = True
#     while i < x // 2 + 1 and flag:
#         if x % i == 0:
#             flag = False
#         i += 1
#     if flag == True:
#         return "YES"
#     return "NO "

# n = int(input("Введи число брат : "))
# print(prost(n))


# 37. Дано натуральное число N и последовательность из N элементов.
# Требуется вывести эту последовательность в обратном порядке.
# Примечание. В программе запрещается объявлять массивы и
# использовать циклы (даже для ввода и вывода).

# Input: 2 -> 3 4
# Output: 4 3

# def f(n):
#     if n == 0:
#         return ''
#     k = int(input())
#     return f(n-1) + " " + str(k)
#     # return f(n-1) + f' {k}'или так

# print(f(int(input())))

# Задача 28: Напишите рекурсивную функцию sum(a, b),
# возвращающую сумму двух целых неотрицательных чисел.
# Из всех арифметических операций допускаются только +1 и -1.
# Также нельзя использовать циклы.
# 2 2
# 4

# n = 15
# p = 6

# def sum(x, y):
#     if x == 0:
#         return y
#     return sum(x-1, y+1)

# print(f' итог: {sum(n, p)}')


# Задача 26: Напишите программу, которая на вход принимает два числа A и B,
# и возводит число А в целую степень B с помощью рекурсии.

# A = 3; B = 5 -> 243 (3⁵)
# A = 2; B = 3 -> 8

# a = int(input("введите число А : "))
# a1 = a
# b = int(input("введите число В : "))
# count = 1
# def st(x, y, z, w):

#     if z == y:
#         return x
#     z += 1
#     return st(x*w, y, z, w)

# print(f' Итог = {st(a, b, count, a1)}')


# 1- в списке храняться числа. Нужно выбрать только четные числа и составить список пар
# (число; квадрат числа).
# пример : 1 2 3 5 8 15 23 38
# Получить : [(2,4),(8,64),(38,1444)]


# data = [1, 2 , 3, 5, 8, 15, 23, 38]
# res = list()

# for i in data:
#     if i%2 == 0:
#         # % 2 == 0 проверка на четность , делится ли без остатка.
#         res.append((i, i**2))
# # append  добавляет в список . а двойные скобки делают картеж.
# print(res)


# БУДЕМ УПРОЩАТЬ
# def select(f, col):
#     return [f(x) for x in col]

# def where(f, col):
#     return [x for x in col if f(x)]

# data = [1, 2 , 3, 5, 8, 15, 23, 38]
# res = select(int, data)
# print(res)
# res = where(lambda x: x % 2 == 0, res)
# print(res)
# res = list(select(lambda x: (x, x**2), res))
# print(res)

# //////////////////////////////////////////////////////////
# data = '15 156 96 3 5 8 52 5'
# # была строка
# print(data)

# data = data.split()
# #переобразовали в список
# print(data)

# data = list(map(int, data.split()))
# #и в этот момент из строки мы получили список с числами и цифрами
# print(data)


# ???????????????????????????????????????????????????????????????????????????????????????

# упрощаем с фунцией "map"

# def where(f, col):
#     return [x for x in col if f(x)]

# data = [1, 2 , 3, 5, 8, 15, 23, 38]
# res = map(int, data)
# print(res)
# res = where(lambda x: x % 2 == 0, res)
# print(res)
# res = list(map(lambda x: (x, x**2), res))
# print(res)

# ????????????????????????????????????????????????????????????????????????????????????????

# ФУНКЦИЯ ФИЛЬТР , ВОЗВРАЩАЕТ ТОЛЬКО ТРУ ЗНАЧЕНИЯ

# data = [15, 65, 9, 36, 175]
# res = list(filter(lambda x: x%10 == 5, data))
# print(res)

# ????????????????????????????????????????????????????????????????????????????????????????

# упрощаем с фунцией "map"
# упрощаем с функцией  "filter"

# data = [1, 2 , 3, 5, 8, 15, 23, 38]
# res = map(int, data)
# res = filter(lambda x: x % 2 == 0, res)
# res = list(map(lambda x: (x, x**2), res))
# print(res)
