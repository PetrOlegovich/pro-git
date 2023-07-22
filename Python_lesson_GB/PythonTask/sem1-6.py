# print(list(range(5)))

# for i in 1, 5, True, 1.56, 'Hello world':
#     print(i)

# for  i in range(5):
#     print(i)

# range(n) - 0, 1, 2..., n-1
#  range(3, n) - 3, 4, 5..., n-1

# for  i in range(3, 10):
#     print(i)

# range(10, 0, -1) - 10, 9, 8, 7, 6, 6, 5, 4, 3, 2, 1
# range(begin, end, step)

# i = 0
# while i < 5:
#     i = i + 1
#     print(i, end=' ')

# i = 0
# while i < 5:
#     i = i + 1 # i +=1
#     if i == 5:
#         print(i)
#     else:
#         print(i, end=', ')

#############################################################################################

#############################################################################################

# Дана последовательность из N целых чисел и число K.
# Необходимо сдвинуть всю последовательность
# (сдвиг - циклический) на K элементов вправо, K – положительное число.

# Input: [1, 2, 3, 4, 5] k = 2

# Output: [4, 5, 1, 2, 3]

# Примечание: Пользователь может вводить значения
#  списка или список задан изначально.


# lst = [1,2,3,4,5,6]
# print(lst)
# k = int(input("на сколько сдвинуть ? :  "))

# for i in range(k):
#     lst.insert(0, lst.pop(-1))                                  # insert добавляет на нужную позицию
# print(f"сдвинули на {k} . вот результат :  {lst}")              # POP - (название списка , название функции , и номер элемента который мы удаляем по номеру )


# list_1 = [1, 2, 3, 4, 5]
# k = int(input())
# k = k % len(list_1)
# list_result = list()

# for i in range(k):
#     list_result.append(list_1[len(list_1) - k + i])

# for i in range(len(list_1) - k):
#     list_result.append(list_1[i])
# print(list_result)


# Напишите программу для печати всех уникальных значений в словаре.
# Input: [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII": " S005 "}, {" V ":" S009 "}, {" VIII ":" S007 "}]
# Output: {'S005', 'S002', 'S007', 'S001', 'S009'}

# Примечание: Список словарей задан изначально. Пользователь его не вводит

# L = [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII": "S005"}, {" V ":" S009 "}, {" VIII ":" S007 "}]
# print(f"огигинал : {L} ")
# u_value = set(val for dic in L for val in dic.values())
# print(f"уникальные значения : {u_value}")


# list_1 = [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII": "S005"}, {"V": "S009"}, {"VIII": "S007"}]
# list_2 = list()
# for i in list_1:
#     for j in i:
#         list_2.append(i[j])

# list_result = list()
# for i in list_2:
#     if i not in list_result:
#         list_result.append(i)
# print(list_result)


# list_1 = [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII": "S005"}, {"V":"S009"}, {"VIII":"S007"}]
# set_1 = set()
# for i in list_1:
#     for j in i:
#         set_1.add(i[j])
# print(set_1)


# Дан массив, состоящий из целых чисел. Напишите программу,
# которая подсчитает количество элементов массива, больших предыдущего
# (элемента с предыдущим номером)


# Input: [0, -1, 5, 2, 3]
# Output: 2 (-1 < 5, 2 < 3)

# Примечание: Пользователь может вводить значения списка или список задан изначально.

# array = [0, -1, 5, 2, 3]

# # for n in range(array):
# #     n = int(input("введите числа массива :  "))

# count = 0
# j = 1
# while j < len(array):
#     if array[j] > array[j-1]:
#         count = count + 1
#         j = j + 1
#     else:
#         j = j + 1
# print(count)


# array = []
# n = int(input("Введите величину массива : "))
# for i in range(0, n):
#     array.append(int(input("Введите элемент массива : ")))                      #Заполнение с клавиатуры
# for i in range(0, n):                                                           # пример с массивом
#     print(array[i])
# print(array)


# array = []
# n = int(input("Введите величину массива : "))
# for i in range(0, n):
#     array.append(int(input("Введите элемент массива : ")))
# print(f'ваш массив : {array}')
# count = 0
# j = 1
# while j < len(array):
#     if array[j] > array[j-1]:
#         count += 1
#         j += 1
#     else:
#         j += 1
# print(f"{count} числа больше предыдущих")


# n = [0, -1, 5, 2, 3]
# cnt = 0
# list_1 = list()
# for i in range(len(n) - 1):
#     if n[i] < n[i + 1]:
#         cnt += 1
#         list_1.append((n[i], n[i + 1]))
# print(f"{cnt} ({', '.join([str(i[0]) + ' < ' + str(i[1]) for i in list_1])})")



# print(text.lower())     #все в н ижнем регисттре
# print(len(word)) # Сколько символов в тексте

#############################################################################################
#############################################################################################

# функция ждоин разделяет  все элементы через разделитель который мы указываем !!!
# list_1 = [1, 5, "hello", 23, -100]
# print(', '.join([str(i) for i in list_1]))

# в примере ниже разделителя нет ('') поэтому все элементы слились
# list_1 = ['h', 'e', 'l', 'l', 'o']
# print(''.join(list_1))

# из строки делает список
# stroka = "hello world Moskow Name"
# print(stroka.split(" "))


# Напишите программу, которая принимает на вход строку,
# и отслеживает, сколько раз каждый символ уже встречался.
# Количество повторов добавляется к символам с помощью постфикса формата _n.

# Input: a a a b c a a d c d d
# Output: a a_1 a_2 b c a_3 a_4 d c_1 d_1 d_2

# Для решения данной задачи используйте функцию .split()
# №1

# text = input("Введите строку : ").split()
# text1 = {}
# for i in text:
#     if i in text1:
#         text1[i] += 1
#         print(f'{i}_{text1[i]}', end=" ")

#     else:
#         print(i, end=' ')
#         text1[i] = 0

# Пользователь вводит текст(строка). Словом считается последовательность
# непробельных символов идущих подряд, слова разделены одним или большим
# числом пробелов. Определите, сколько различных слов содержится в этом тексте.

# Input:
# She sells sea shells on the sea shore The shells that
# she sells are sea shells I'm sure So if she sells sea
# shells on the sea shore I'm sure that the shells are
# sea shore shells

# Output: 13


#
# print(len(set(input().lower().split())))


# ПОЯСНИТЕЛЬНАЯ БРИГАДА :
# input - вводим текст
# lower - переводит все в нижний регистр (т.к. одинаковые слова в разных регистрах - это разные слова ).
#           и одинаковые слова (мЯч и мяч ) станут ваистину одинаковыми
# split - создаем список , где каждый элемент записан отдельно
# set - идет преобразование в сет. в множество . а в множестве не может быть повторяющихся элементов
# len - посчитаем количество множества.


# text = input().split()
# set_result = set()
# for i in text:
#     set_result.add(i.lower())
# print(len(set_result))
# ТУт все тоже самое. только не в 1 строку .


# Задача 22: Даны два неупорядоченных набора целых чисел (может быть, с повторениями).
#  Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
# Пользователь вводит 2 числа. n - кол-во элементов первого множества.
# m - кол-во элементов второго множества. Затем пользователь вводит сами элементы множеств.


# n = int(input("Введите размер множества N : "))
# m = int(input("введите размер множества M : "))
# firstNumbers = set()
# doubleNumbers = set()                               #создал пустые множества
# for i in range(n):
#     firstNumbers.add(int(input("числа  N : ")))         # заполняю пустое множество с клавиатуры и сразу перевожу в инт ( для вывода по порядку)
# for i in range(m):
#     doubleNumbers.add(int(input("числа  M  : ")))
# unique = firstNumbers.union(doubleNumbers)          # обьеденяю множества в 1 целое
# print(unique)





# РАЗВОРОТ МАССИВА !!!!!!

# for (i = 0; i <=count/2; i++) {
#      var t  =  arr[count-i];
#      arr[count-i]=arr[i];
#      arr[i] = t;
# }
