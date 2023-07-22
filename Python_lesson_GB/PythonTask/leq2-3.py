# ФУГКЦИИ

# def sumNumbers(n):
#     summa = 0
#     for i in range(1, n+1):
#         summa += i
#     return summa      # ретёрн заканчивает функцию .
#     print('stop')     # не выведет стоп. т.к. ретерн уже завершил функцию

# a = sumNumbers(5)
# print(a)

# def sum_str(*args):
#     res = ''
#     for i in args:
#         res += i
#     return res
# print(sum_str('q', 'e', 'l'))
# print(sum_str('q', 'e', 'l', 'r', 'f'))




# import modul1                                 # вызов функции из другого файла
# print(modul1.max1(5, 9))

# from modul1 import max1
# print(max1(16, 9))                            # вызов определенной функции с файла модуль1

# from modul1 import *                          # вызов всех функций из файла модуль1
# print(max1(16, 9))

# import modul1 as m1                             #импортируем модуль и меняем его название для удобства
# print(m1.max1(17, 9))


# Рекурсия по поиску числа фибоначи
# def fib(n):
#     if n in [1,2]:
#         return 1
#     return fib(n-1) + fib(n-2)

# list_1 = []
# for i in range(1, 10):
#     list_1.append(fib(i))
# print(list_1)


# Бинарная сортировка !  Бинарная сортировка !  Бинарная сортировка !  Бинарная сортировка !  Бинарная сортировка !


#Быстрая сортировка :

# def quick_sort(array):
#     if len(array) <= 1:
#         return array
#     else:
#         pivot = array[0]
#     less = [i for i in array[1:] if  i <= pivot]
#     greater = [i for i in array[1:] if  i > pivot]
#     return quick_sort(less) + [pivot] + quick_sort(greater)

# print(quick_sort([10, 5, 2]))


# Сортировка слиянием:

# def merge_sort(nums):
#     if len(nums) > 1:
#         mid = len(nums) // 2
#         left = nums[:mid]
#         right = nums[mid:]
#         merge_sort(left)
#         merge_sort(right)
#         i = j = k = 0
#         while i < len(left) and j < len(right):
#             if left[i] < right[j]:
#                 nums[k] = left[i]
#                 i +=1
#             else:
#                 nums[k] = right[j]
#                 j +=1
#             k +=1
#         while i < len(left):
#             nums[k] = left[i]
#             i += 1
#             k += 1
#         while j < len(right):
#             nums[k] = right[j]
#             j += 1
#             k += 1
# list_1 = [1,5,6,9,8,7,2,1,55,22,2,4,5,8,4,7,3,49,85]
# merge_sort(list_1)
# print(list_1)



##############################################################################################
##############################################################################################

# def f(x):
#     return x*x

# print(f(5))
# print(type(f))
# a = f
# print(type(a))
# print(a(4))


# def calk1(a, b):
#     return a+b
# # calk1 = lambda a,b: a + b


# def calk2(a, b):
#     return a*b

# def math(op, x, y):
#     print(op(x, y))

# math(lambda a,b: a + b, 5, 45)


# list1 = [1, 2 , 3, 5, 6, 7, 8, 9, 10, 15, 23, 38]

# def qwa(x):
#     for i in x:
#         if i % 2 == 0:
#             print(i, i*i)
# qwa(list1)




# data = [1, 2 , 3, 5, 6, 7, 8, 9, 10, 15, 23, 38]
# res = list()
# for i in data:
#     if i % 2 == 0:
#         res.append((i, i**2))
# print(res)


# data = [1, 2 , 3, 5, 6, 7, 8, 9, 10, 15, 23, 38]
# def select(f, col):
#     return [f(x) for x in col]

# def where(f, col):
#     return [x for x in col if f(x)]
# res = select(int, data)
# print(res)
# res = where(lambda x: x % 2 == 0, res)
# print(res)
# res = list(select(lambda x: (x, x**2), res))
# print(res)


# list1 = [x for x in range(1, 20)]
# print(list1)
# list1 = list(map(lambda x: x+10, list1))
# print(list1)


# data  = '5 15 14 17 18 16 458 554'
# data = list(map(int, data.split()))
# print(data)


# data = [1, 2 , 3, 5, 7, 8, 9, 15, 23, 38]
# def where(f, col):
#     return [x for x in col if f(x)]
# res = map(int, data)
# print(res)
# res = where(lambda x: x % 2 == 0, res)
# print(res)
# res = list(map(lambda x: (x, x**2), res))
# print(res)



# data = [15, 65, 9, 36, 175]
# res = list(filter(lambda x: x % 10 == 5 , data))
# print(res)



# data = [1, 2 , 3, 5, 7, 8, 9, 15, 23, 38]

# res = map(int, data)
# res = filter(lambda x: x % 2 == 0, res)
# res = list(map(lambda x: (x, x**2), res))
# print(res)