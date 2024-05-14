# str_ = "Строка с цифрой 1"
#
# is_substr = "Строка" in str_ # True
# print ("В строке есть слово строка?", is_substr)

# number = 12
# condition_1 = number % 2 == 0 #Число кратно 2
# condition_2 = number % 3 == 0 #Число кратно 3
#
# if condition_1 and condition_2:
#     print ('Число кратно 2 и 3')
# else:
#     print ('Число не (кратно 2 и 3)')

# mount = 12
#
# # символ \ позволяет визуально разбить команду, для интерперататора это одна строка
# bad_condition = \
# mount == 12 or \
#     mount == 1 or \
#     mount == 2 # ОЧень плохая запись условия
# good_condition = mount in [12,1,2] # При множественном сравнении лучше использовать in
#
# if good_condition:
#     print ("Зимаа!!!")

# hour = 7
# bad_condition = (6 <= hour) and (hour < 12) # цепочки операторов всегда соединяются через AND
# good_condition = 6 <= hour < 12
#
# if good_condition:
#     print("Утро!")

# list_ = [5, 6, 7, 8, 9]
#
# result = (4 in list_) and (8 in list_)
# print(result)

# month = 15
# # Создание списков с месяцами для каждого сезона
#
# # Проверка значения переменной month для определения сезона
#   # Если month находится в списке весенних месяцев, выводим "Весна"
#   # Если month находится в списке летних месяцев, выводим "Лето"
#    # Если month находится в списке осенних месяцев, выводим "Осень"
#     # Если month находится в списке зимних месяцев, выводим "Зима"
# if month > 12:
#  print ('Не может быть')
# elif month < 12:
#  print ('Существует')
# else:
#     print ('Существует')

# is_logged_in = 1
#
# is_logged_in_bad = \
#  is_logged_in == 1
#
# is_logged_in_good = is_logged_in in [1] #Ответ будет да.
#
# is_logged_in_bad = is_logged_in in [0] #Ответ будет нет.
#
# if is_logged_in_good:
#     print("Пользователь вошёл в систему")
# elif is_logged_in_bad:
#     print("Пользователь не вошёл в систему")
#
# has_items_in_cart = 1
#
# has_items_in_cart_bad = \
#  has_items_in_cart == 1
#
# has_items_in_cart_good = has_items_in_cart_bad in [1] #Ответ будет да.
#
# has_items_in_cart_bad = has_items_in_cart in [0] #Ответ будет нет.
#
# if has_items_in_cart_good:
#     print("В Корзине есть товаров")
# elif has_items_in_cart_bad:
#     print("В корзине нету товаров")
#
# has_shipping_address = 1
#
# has_shipping_address_bad = \
#  has_shipping_address == 1
#
# has_shipping_address_good = has_shipping_address_bad in [1] #Ответ будет да.
#
# has_shipping_address_bad = has_shipping_address in [0] #Ответ будет нет.
#
# if has_shipping_address_good:
#     print("Пользователь ввёл адрес")
# elif has_shipping_address_bad:
#     print("Пользователь нету адреса")
#
# total_purchase = 1
#
# total_purchase_bad = \
# total_purchase == 1
#
# total_purchase_good = has_shipping_address_bad and has_items_in_cart_bad and is_logged_in_bad in [1]
#
# total_purchase_bad =  has_shipping_address and has_items_in_cart and is_logged_in in [0]
#
# if total_purchase_good:
#     print ("Пользователь ввёл верные данные")
# elif total_purchase_bad:
#     print ("Пользователь ввёл неверные данные")