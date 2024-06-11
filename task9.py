# k,l = list(range(1,11)), list(range(1,11))
#
# for i in range(1,11):
#     k[i-1] = 10 - i
# for i in range(1,11):
#     l[i-1] = k[5] - k[i-1]
# print(k)
# print(l)
# print(f'Количество отрицательных элементов массива l = {len([value for value in l if value < 0])}')

# k,l = list(range(1,11)), list(range(1,11))
#
# for n in range(1,11):
#     k[n-1] = 10 - n
# for n in range(1,11):
#     l[n-1] = k[7] - k[n-1]
# print(k)
# print(l)
# print(f'Количества положительных элементов массива l = {len([value for value in l if value > 0])}')

# a, b = list(range(1, 11)), list(range(1, 11))
#
# for i in range(1, 11):
#     a[i-1] = 10 - i
# for i in range(1, 11):
#     b[i-1] = a[5] - a[i-1]
# print(a)
# print(b)
# print(f'Количества отрицательных элементов l = {len([value for value in b if value < 0])}')

# k,l = list(range(1, 11)), list(range(1, 11))
#
# for i in range(1,11):
#     k[i - 1] = 10 - i
# for i in range(1,11):
#     l[i - 1] = k[5] - k[i - 1]
# print(k)
# print(l)
# # count_k = 0
# # for value in k:
# #     if value < 0:
# #         count_k += 1
# # count_l = 0
# # for value in l:
# #     if value < 0:
# #         count_l += 1
# # print(f'Количество отрицательных элементов = {count_k + count_l}')
# count_k = len([value for value in k if value < 0])
# count_l = len([value for value in l if value < 0])
# print(f'Количество отрицательных элементов = {count_k + count_l}')

# field = [ # поле 3х3 с крестиками и ноликам
#  ["X", "O", "X"], #Первая строка таблицы
#  ["O","X","O"], # вторая строка таблицы
#  ["X","O","X"], # третья строка таблицы
# ]
# # for i in field:
# #     f =""
# #     for n in i:
# #         f+=n + " "
# #     print(f)
#
# for row in field:
#  for cell in row:
#     print(cell, end=" ")
#  print()

heads = 35  # Общее количество голов
legs = 94  # Общее количество лап

for rabbits in range(heads + 1):
    for pheasants in range(heads + 1):
        total_legs = 4 * rabbits + 2 * pheasants
        if total_legs > legs:
            continue  # Пропускаем подсчет голов, если количество лап превышает допустимое
        if rabbits + pheasants == heads and total_legs == legs:
            print("Кролики:", rabbits)
            print("Фазаны:", pheasants)
