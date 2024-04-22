#Задача №1
bytes = 4 #один символ
disk = 1,44 #МБ объём дискеты
page = 100 #Количество страниц
str = 50 #количество строк
charge = 25 #Символ в строке

#Рассчёты
a = charge * bytes
max_disk = 1.44*1024*1024
listsbook = max_disk//(page*str*a)
print ("Количество одинаковых книг", listsbook)

#Задача №2
pi = 3.1415
radius = 5^2
perimeter = 4 * radius
side = 5
area = pi * radius
area = round (area,2)
circumference = 2*pi*radius
circumference = round (circumference,2)
perimeter_square = 4*side
square_area = side^2
print("Площадь круга", area)
print("Длина окружности",circumference)
print("Площадь квадрата",square_area)
print ("Периметр квадрата",perimeter_square)



