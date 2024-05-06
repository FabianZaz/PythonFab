# a = [1,2.1,3] #Раньше я был списком
# tuple(a) #(1,2.1,3), но 'a' остался списком
# b = tiple('abc') # ('a','b','c')
# a = (1,1.1, 'a')
# print(a) # (1,1.1,'a')
#
# a= (1,1.1,'a')
# a[0] = 'a' #Ошибка.
# a = (1,2,3) # Теперь 'a' равно (1,2,3)
# a = (1,1.1, 'a')
# del a[0] #Ошибка
# del a #Полное удаление переменной "a"
#
# a = (1,2,3) # Это одномерный кортеж
# b = ((1,2,3),(4,5,6),(7,8,9)) # Это двумерный (кортеж в кортеже) кортеж. Его можно пресдтавить как ((1,2,3),(4,5,6),(7,8,9))

# a = (1,2,3)
# b = (4,5,6)
# c = a + b
# print(c)
# a += b

# a = (1,2,3)
# b = 2
# c = a * b
# print(c)


# a = (1,2,1)
# a.count(1)
# a.index(2)
# print(a.count)
#
# empty_tuple = () # Пустой кортеж
# tuple_with_one_item = (1,) # кортеж из одного элемента
# tuple_ = (1, 2, "str")
# print("Содержимое переменной empty_tuple:", empty_tuple,
# type(empty_tuple))
# print("Содержимое переменной tuple_with_one_item:",
# tuple_with_one_item, type(tuple_with_one_item))
# print("Содержимое переменной tuple_:", tuple_, type(tuple_))
# list_ = [] # Пустой список
# chars_list = ["a", "b", "c"]
# print("Содержимое переменной list_:", list_, type(list_))
# print("Содержимое переменной chars_list:", chars_list,
# type(chars_list))
# empty_string = "" # Пустая строка
# str_ = "test" # Строковый тип данных
# print("Содержимое переменной empty_string:", empty_string,
# type(empty_string))
# print("Содержимое переменной str_:", str_, type(str_))
# empty_set = set() # Пустое множество
# set_ = {3, 2, 1, 1} # Множество содержит в себе только уникальные элементы
# print("Содержимое переменной empty_set:", empty_set,
# type(empty_set))
# print("Содержимое переменной set_:", set_, type(set_))
# empty_dict = {} # Пустой словарь
# dict_ = { # Словарь хранит пары ключ-значение. Ключи должны
# #быть уникальными значениями
#  "Имя": "Ваше имя",
#  "Фамилия": "Ваша фамилия",
#  "Возраст": 18,
#  "Возраст": 20,}
# print("Содержимое переменной empty_dict:", empty_dict,
# type(empty_dict))
# print("Содержимое переменной dict_:", dict_, type(dict_))

# list_players = ["Маша", "Петя", "Саша", "Оля", "Кирилл"]
# last_players = list_players[-1]
# reestr = {"Первый участник": list_players[0]}
#
# print("Последний участник:",last_players)
# print("Первый участник:", reestr ["Первый участник"])

# list_participants = ["Орлов", "Петров", "Иванов", "Сидоров", "Васильев", "Черепахин"]
# last_participant = list_participants[-1]
# winner = {"Первый лыжник": list_participants[0]}
# print("Последний лыжник:",last_participant)
# print("Первый лыжник:",winner ["Первый лыжник"])

# sps_book = ["Дубровский", "Горе от ума","Кавказский пленник","Хамелеон","Ревизор", "Гранатовый браслет"]
# last_book = sps_book[-1]
# pushkin = {"Первая книга": sps_book[0]}
# print("Последний книга:", last_book)
# print("Первый книга:",pushkin ["Первая книга"])

