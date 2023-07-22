# 1.Есть список a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89].
# Выведите все элементы, которые меньше 5.

# a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

#         # мое решение :
# b = []
# for i in range(len(a)):
#     if a[i] < 5:
#         b.append(a[i])
# print(b)

#         # интернет:
# for elem in a:
#     if elem < 5:
#         print(elem)
#         # интернет:
# print(list(filter(lambda elem: elem < 5, a)))
#         # интернет:
# print([elem for elem in a if elem < 5])


# № № № № # № № № № # № № № № # № № № № # № № № № # № № № № # № № № № # № № № № # № № № № # № № № № # № № № № # № № № №
# № № № № # № № № № # № № № № # № № № № # № № № № # № № № № # № № № № # № № № № # № № № № # № № № № # № № № № # № № № №


# 2.Даны списки:

# a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89];
# b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13].
# Нужно вернуть список, который состоит из элементов, общих для этих двух списков.

# a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

# my dicision:
# c = []
# for i in range(len(a)):
#     for j in range(len(b)):
#         if a[i] == b[j]:
#             c.append(a[i])
# print(c)
# internet:
# result = list(filter(lambda elem: elem in b, a))
# print(result)
# internet:
# result = [elem for elem in a if elem in b]
# print(result)
# internet: переводит в множества . и все дубли удаляются.
# result = list(set(a) & set(b))
# print(result)

# № № № № # № № № № # № № № № # № № № № # № № № № # № № № № # № № № № # № № № № # № № № № # № № № № # № № № № # № № № №
# № № № № # № № № № # № № № № # № № № № # № № № № # № № № № # № № № № # № № № № # № № № № # № № № № # № № № № # № № № №

# 3.Отсортируйте словарь по значению в порядке возрастания и убывания.

# dictionary = {'up': 2, 'right': 4, 'left': 7, 'down': 18, 'rightf': 5 }
#             #с помощью из интернета:
# sort = dict(sorted(dictionary.items(), key=lambda item: item[1]))
# print(sort)

# sorted_values = sorted(dictionary.values()) #сортировка словаря по значению
# new_sorted_dictionary = {}
# for i in sorted_values:
#     for j in dictionary.keys():
#         if dictionary[j] == i:
#             new_sorted_dictionary[j] = dictionary[j]
#             break
# print(new_sorted_dictionary)

# крутое решение из интернета :
# по возрастанию:
# import operator
# d = {'up': 2, 'right': 4, 'left': 7, 'down': 18, 'rightf': 5 }
# result = dict(sorted(d.items(), key=operator.itemgetter(1)))
# print(result)
# по убыванию:
# result = dict(sorted(d.items(), key=operator.itemgetter(1), reverse=True))
# print(result)


# № № № № # № № № № # № № № № # № № № № # № № № № # № № № № # № № № № # № № № № # № № № № # № № № № # № № № № # № № № №
# № № № № # № № № № # № № № № # № № № № # № № № № # № № № № # № № № № # № № № № # № № № № # № № № № # № № № № # № № № №

# 4 Напишите программу для слияния нескольких словарей в один.
# моё решение. для 2х подходит , далее нет.
# dictionary = {'up': 2, 'right': 4, 'left': 7, 'down': 18, 'rightf': 5 }
# my_dict = {'a':500, 'b':5874, 'c': 560,'d':400, 'e':5874, 'f': 20}
# new_dict = {}

# for i in dictionary:
#     new_dict[i] = dictionary[i]
# for j in my_dict:
#     new_dict[j] = my_dict[j]
# print(new_dict)

# из интернета:
# dict_a = {1:10, 2:20}
# dict_b = {3:30, 4:40}
# dict_c = {5:50, 6:60}

# result = {}
# for d in (dict_a, dict_b, dict_c):
#     result.update(d)
# print(result)

# # update() обновляет/дополняет словарь dict с помощью пар ключ-значение из other ,
# # перезаписывая существующие ключи новыми значениями из other . Если ключ в словаре отсутствует,
# # то он добавляется. Метод ничего не возвращает.


# из интернета:
# dict_a = {1:10, 2:20}
# dict_b = {3:30, 4:40}
# dict_c = {5:50, 6:60}
# result = {**dict_a, **dict_b, **dict_c}
# print(result)


# № № № № # № № № № # № № № № # № № № № # № № № № # № № № № # № № № № # № № № № # № № № № # № № № № # № № № № # № № № №
# № № № № # № № № № # № № № № # № № № № # № № № № # № № № № # № № № № # № № № № # № № № № # № № № № # № № № № # № № № №


# 5. Найдите три ключа с самыми высокими значениями в словаре
# my_dict = {'a':500, 'b':5874, 'c': 560,'d':400, 'e':5874, 'f': 20}.

# my_dict = {'a':500, 'b':5874, 'c': 560,'d':400, 'e':5874, 'f': 20}
# print(sorted(my_dict.values())[-3:])

# вывод сортировонного значения на возрастание
#  и забираем только три последних. тоесть самые максимальные


# list_1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# print(list_1[0])     # 1
# print(list_1[1])     # 2
# print(list_1[-1])    # 10
# print(list_1[-5])    # 6
# print(list_1[:])     # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# print(list_1[:2])    #[1, 2]
# print(list_1[len(list_1)-2:])       # [9, 10]
# print(list_1[2:9])                  # [3, 4, 5, 6, 7, 8, 9,]
# print(list_1[6:-18])                # []
# print(list_1[0:len(list_1):6])      #  [1, 7]
# print(list_1[::6])                  #  [1, 7]


# № № № № # № № № № # № № № № # № № № № # № № № № # № № № № # № № № № # № № № № # № № № № # № № № № # № № № № # № № № №
# № № № № # № № № № # № № № № # № № № № # № № № № # № № № № # № № № № # № № № № # № № № № # № № № № # № № № № # № № № №

# 6. Напишите код, который переводит целое число в строку, при том что его можно применить в любой системе счисления.

# x = 15
# print(type(int(x)))
# print(0)
# print(type(float(x)))
# print(0)
# print(type(str(x)))


# № № № № # № № № № # № № № № # № № № № # № № № № # № № № № # № № № № # № № № № # № № № № # № № № № # № № № № # № № № №
# № № № № # № № № № # № № № № # № № № № # № № № № # № № № № # № № № № # № № № № # № № № № # № № № № # № № № № # № № № №

# 7. Нужно вывести первые n строк треугольника Паскаля.
# В этом треугольнике на вершине и по бокам стоят единицы,
# а каждое число внутри равно сумме двух расположенных над ним чисел.

# def PrintPasTriangle(rows):
#     row = [1]
#     for i in range(rows):
#         print(row)
#         row = [sum(x) for x in zip([0]+row, row+[0])]

# PrintPasTriangle(10)


# def next_row(row):
#     row = [1] + row
#     for i in range(1, len(row)-1):
#         row[i] += row[i+1]
#     return row

# row = []

# for i in range(5):
#     row = next_row(row)
#     print(row)


# не понятно


# № № № № # № № № № # № № № № # № № № № # № № № № # № № № № # № № № № # № № № № # № № № № # № № № № # № № № № # № № № №
# № № № № # № № № № # № № № № # № № № № # № № № № # № № № № # № № № № # № № № № # № № № № # № № № № # № № № № # № № № №


# 8.Напишите проверку на то, является ли строка палиндромом.
# Палиндром — это слово или фраза, которые одинаково читаются слева направо и справа налево.

# x = input("введите слово на проверку его на паллиндротизм : ")
# word = x.lower()
# y = ''.join(reversed(word))    # эта функция разворачивает слово зеркально )))))
# if word == y:
#     print("это палиндром")
# else:
#     print("no bro (((")


# № № № № # № № № № # № № № № # № № № № # № № № № # № № № № # № № № № # № № № № # № № № № # № № № № # № № № № # № № № №
# № № № № # № № № № # № № № № # № № № № # № № № № # № № № № # № № № № # № № № № # № № № № # № № № № # № № № № # № № № №


# 9. Сделайте так, чтобы число секунд отображалось в виде дни:часы:минуты:секунды.

# x = int(input("введи число "))
# day = 86400
# hour = 3600
# minyt = 60
# cDay, cHour, cMinyt = 0, 0, 0
# while x > minyt:
#     if x > day:
#         cDay = int(x/day)
#         x = x - (cDay*day)
#     if x > hour:
#         cHour = int(x/hour)
#         x = x - (cHour*hour)
#     if x > minyt:
#         cMinyt = int(x/minyt)
#         x = x - (cMinyt*minyt)
# print(f"{cDay} дней, {cHour} часов, {cMinyt} минут, {x} секунд")


# № № № № # № № № № # № № № № # № № № № # № № № № # № № № № # № № № № # № № № № # № № № № # № № № № # № № № № # № № № №
# № № № № # № № № № # № № № № # № № № № # № № № № # № № № № # № № № № # № № № № # № № № № # № № № № # № № № № # № № № №


# 10.       Вы принимаете от пользователя последовательность чисел, разделённых запятой.
#           Составьте список и кортеж с этими числами.


# x = input("введи числа через запятую")
# xx = x.split(',')

# print(xx)
# print(type(xx))

# y = tuple(xx)

# print(y)
# print(type(y))


# № № № № # № № № № # № № № № # № № № № # № № № № # № № № № # № № № № # № № № № # № № № № # № № № № # № № № № # № № № №
# № № № № # № № № № # № № № № # № № № № # № № № № # № № № № # № № № № # № № № № # № № № № # № № № № # № № № № # № № № №

# 11. Выведите первый и последний элемент списка.

# list_1 = [1, 2, 3, 4, 5, 6]
# print(f"{list_1[0]}   {list_1[-1]}")


# № № № № # № № № № # № № № № # № № № № # № № № № # № № № № # № № № № # № № № № # № № № № # № № № № # № № № № # № № № №
# № № № № # № № № № # № № № № # № № № № # № № № № # № № № № # № № № № # № № № № # № № № № # № № № № # № № № № # № № № №

# 12.Напишите программу, которая принимает имя файла и выводит его расширение.
# Если расширение у файла определить невозможно, выбросите исключение.

# x = input("введите имя файла целиком : ")
# ras = x.split('.')
# if len(ras) > 1 and len(ras) < 3:
#     if len(ras) > 2:
#         print("невозможно узнать расширение 1")
#     print(f" Расширение файла : .{ras[1]}")
# else:
#     print("невозможно узнать расширение")


# № № № № # № № № № # № № № № # № № № № # № № № № # № № № № # № № № № # № № № № # № № № № # № № № № # № № № № # № № № №
# № № № № # № № № № # № № № № # № № № № # № № № № # № № № № # № № № № # № № № № # № № № № # № № № № # № № № № # № № № №

# 13.