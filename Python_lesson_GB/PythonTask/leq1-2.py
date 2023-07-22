# a= 5
# b = 6.76
# c = 'hello'


# print(a,' - ', b,' - ',c)
# print(f"{a} - {b} - {c}")
# print("{} - {} - {}".format(a,b,c))

# print("введите первую строку: ")
# a = input()
# print(a)

# print('введите первоое число ')
# a = int(input())
# b = int(input('Введите второе число  '))
# print(a, ' + ', b, ' = ', a + b)

# a = 5.5845751
# b = 7.558
# print(round(a*b, 3))

# iter = 2
# iter += 3 #  iter = iter + 3
# iter -= 4 #  iter = iter - 4
# iter *= 5 #  iter = iter * 5
# iter /= 5 #  iter = iter / 5
# iter //= 5 #  iter = iter // 5
# iter %= 5 #  iter = iter % 5
# iter **= 5 #  iter = iter ** 5 (возводит в 5ю степень)



# a = 'qwerty'
# for i in a:
#     print(i)

line = ""
for i in range(5):
    line = " "
    for j in range(5):
        line += "* "
    print(line)

# text = 'СъЕШЬ ещё этих МяГкИх французских булок'
# print(len(text))        #сколько символов в тексте
# print('ещё' in text)    # ищет слова  или часть слова
# print(text.lower())     #все в н ижнем регисттре
# print(text.upper())       # переводит в большой регистр
# print(text.replace('ещё','ЕЩЁ'))  # Замена слова или части слова или буквы или знака

############################################################################################################
############################################################################################################\


# list_1 = [1, 5]
# print(list_1)
# list_1.append(8)
# print(list_1)
# list_1.append(89)
# print(list_1)


# list_1 = []
# print(list_1)
# for i in range(5):
#     list_1.append(i)
#     print(list_1)


# Удаление последнего элемента списка
# list_1 = [12, 7, -1, 21, 0]
# print(list_1.pop()) #0
# print(list_1) # [12, 7, -1, 21]
# print(list_1.pop()) # 21
# print(list_1)  # [12, 7, -1]
# print(list_1.pop()) # -1
# print(list_1) # [12, 7]


# Удаление конкретного элемента из списка
# list_1 = [12, 7, -1, 21, 0]
# print(list_1.pop(0)) # 12
# print(list_1) # [7, -1, 21, 0]


# Добавление элемента на нужную позицию
# list_1 = [12, 7, -1, 21, 0]
# print(list_1.insert(2, 11))
# print(list_1) # [12, 7, 11, -1, 21, 0]




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


# КОРТЕЖИИИИ  И И И И И И ИИ И И И И И ИИ И И И И И И ИИ И И И ИИ И И И
# t = ()

# print(type(t))

# t = (1, 5, 3,)
# print(type(t))

v = [1, 8, 9]
# print(v)
# print(type(v))

v = tuple(v)
print(v)
print(type(v))

# a, b, c = v

# print(a, b, c)



# t = (1, 2, 3, 5,)
# for i in t:
#     print(i)

# t = (1, 2, 3, 5,)
# for i in range(len(t)):
#     print(t[i])



##################### СЛОВАРИ

# d = {}
# d = dict()

# d['q'] = 'qwertty'
# print(d)

# d['w'] = 'wertty'
# print(d)

# print(d['q'])
# print(d['w'])


# dictionary = {}
# dictionary = {'up': '↑', 'right': '→', 'left': '←', 'down': '↓', 'right': '→' }
# print(dictionary) # {'up': '↑', 'left': '←', 'down': '↓', 'right': '→' }             ☚
# print(dictionary['left']) # ←
# # типы ключей могут отличаться
# print(dictionary['up'])  # ↑
# # типы ключей могут отличаться
# dictionary['left'] = '☚'
# print(dictionary['left']) # ☚
# print(dictionary['type']) # KeyError: 'type'
# del dictionary['left']  # удаление элемента
# for item in dictionary:         # for (k, v) in dictionary.items():
#     print('{}: {}'.format(item, dictionary[item]))

# dictionary = {}
# dictionary = {'up': '↑', 'left': '←', 'down': '↓', 'right': '→' }

# # del dictionary['left']  # удаление элемента
# for item in dictionary:         # for (k, v) in dictionary.items():
#     print('{}: {}'.format(item, dictionary[item]))
#     # print(item)



# dictionary = {}
# dictionary = {'up': '↑', 'left': '←', 'down': '↓', 'right': '→' }

# print(dictionary.items())
# for (k, v) in dictionary.items():
#     print(k, v)
# #     # print(item)




# colors = {'red', 'green', 'blue'}
# print(colors)           # {'red', 'green', 'blue'}
# colors.add('red')
# print(colors)           # {'red', 'green', 'blue'}
# colors.add('gray')
# print(colors)           # {'red', 'green', 'blue', 'gray'}
# colors.remove('red')
# print(colors)           # {'green', 'blue', 'gray'}
# #colors.remove('red')    # KeyError: 'red'
# colors.discard('red')   # ok
# print(colors)           # {'green', 'blue', 'gray'}
# colors.clear()          # { }
# print(colors)           # set()



# ОПЕРАЦИИ СО МНОЖЕСТВАМИ

# a = {1, 2, 3, 5, 8}
# b = {2, 5, 8, 13, 21}
# c = a.copy()                                # c = {1,2,3,5,8}
# u = a.union(b)                              # u = {1,2,3,5,8,13,21}
# i = a.intersection(b)                       # i = {8,2,5}
# dl = a.difference(b)                        # dl = {1,3}
# dr = b.difference(a)                        # dr = {13,21}
# q=a.union(b).difference(a.intersection(b))  #  { 1,21,3,13}


# a = {1, 8, 6}
# b = frozenset(a)
# print(b)
