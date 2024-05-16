#Task 1

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

#Task 2

# is_logged_in = True
# has_items_in_cart = True
# has_shipping_address = True
# has_order = False
#
# if is_logged_in and has_items_in_cart and has_shipping_address:
#     print("Заказ оформлен успешно")
#     has_order = True
# else:
#     print("Не все критерии для оформления заказа выполнены. Пожалуйста, проверьте информацию")
#
# total_purchase = 1500
# min_purchase = 1000
# is_first_order = False
#
# if has_order and (total_purchase > min_purchase or is_first_order):
#     print("Вы получаете скидку!")


# number = int(input("Введите число:"))
# # print("Вы ввели число:", number)
#
# if number in [7, 13, 21]:
#     print("Счастливое число")
# if number in range(1, 101):
#     print("Число в указанном диапазоне")
# else:
#     print("Не повезло")

