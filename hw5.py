# n1
# Напишите программу, которая определяет уровень персонажа в компьютерной игре. Пользователь вводит число «очков опыта», а программа вычисляет уровень. Новый уровень даётся при достижении 1000, 2500 и 5000 «очков опыта». Начальный уровень равен единице.
# a = int(input("Введите количество опыта: "))
# if a < 1000:
#     print("Ваш уровень - 1")
# elif 2500 > a >= 1000:
#     print("Ваш левел - 2")
# elif 5000 > a >= 2500:
#     print("Ваш левел - 3")
# else:
#     print("Ваш левел - 4")
#


# n2 Напишите программу, которая находит максимум из трёх чисел, не используя дополнительные переменные.

# a = int(input("Введите первое число: "))
# b = int(input("Введите второе число: "))
# c = int(input("Введите третье число: "))
# if c < a > b:
#     print(a)
# elif a < b > c:
#     print(b)
# else:
#     print(c)

# n3 Напишите программу, которая получает от пользователя число X и вычисляет значение функции Y по следующей схеме:

# x = int(input("Введите число х: "))
# if x > 0:
#     y = x - 12
#     print(y)
# elif x < 0:
#     y = x ** 2
#     print(y)
# elif x == 0:
#     y = 5
#     print(y)


# n4  Напишите программу, которая получает на вход место студента в списке и его балл
# а затем выводит соответствующие сообщения о поступлении и получении стипендии.

# a = int(input("Введите место в списке поступающих: "))
# b = int(input("Введите колличество баллов: "))
# if a <= 10 and b == 290:
#     print("Поздровляю вы поступили!, но не хватало баллов на стипендию")
# elif b > 290:
#     print("Поздровляю вы поступили!, бонусом будет начисляться стипендия")
# else:
#     print("Вы не поступили")


# n5
# rating = int(input('Что получил по математике? '))
# if rating == 2:
#  print('Плохо. Марш учиться!')
# if rating == 3:
#  print('Плохо. Марш учиться!')
# if rating == 4:
#  print('Молодец! Можешь отдохнуть.')
# if rating == 5:
#  print('Молодец! Можешь отдохнуть.')

# Скопируйте программу в редактор и оптимизируйте

# rating = int(input('Что получил по математике? '))
# if rating == 5 or rating == 4:
#     print("Молодец можешь отдохнуть!")
# elif rating == 3 or rating == 2:
#     print("Плохо. Марш учиться!")


# n6
# Напишите программу, которая получает на вход число и проверяет, двузначное оно или нет.
# Выведите соответствующее сообщение. Числа −42 и −99 тоже считаются двузначными.
# Сделайте это, используя не более одного оператора if-elsе. Не используйте elif.

# a = int(input("Введите двухзначное число: "))
# if 10 <= a <= 99 or -10 >= a >= -99:
#     print("Число двухзначное")
# else:
#     print("Число не двухзначное")

# n7 Даны три целых числа. Определите, сколько среди них совпадающих. Программа должна вывести одно из чисел
# 3 (если все совпадают), 2 (если два совпадают) или 0 (если все числа различны).

# a = int(input("Введите первое число: "))
# b = int(input("Введите второе число: "))
# c = int(input("Введите третье число: "))
# if a == b == c:
#     print(3)
# elif a == b != c:
#     print(2)
# elif a != b == c:
#     print(2)
# elif a == c !=b:
#     print(2)
# else:
#     print(0)

# n8
# Взять квартиру попросторнее (не менее 100 м2), но стоимостью не более 10 млн.
# Немного расширить круг поиска, то есть взять квартиру поменьше (от 80 м2), но и стоимостью не более 7 млн.
# Напишите программу, которая получает на вход стоимость квартиры и её площадь и выводит сообщение о том, подходит она или нет.

# a = int(input("Введите стоимость квартиры: "))
# b = int(input("Введите площадь квартиры: "))
# if a == 10000000 and b == 100 or a == 7000000 and b == 80:
#     print("Такая квартира подходит")
# else:
#     print("Не подходит")

# n9




# n10
# Напишите программу, которая получает на вход время в часах — число от 0 до 23 — и пишет, можно ли в этот час получить посылку. Используйте только один условный оператор if-else, без elif и прочего. Решите задание двумя способами:
#
# При выполнении условия выводится сообщение: «Можно получить посылку».
# При выполнении условия выводится сообщение: «Посылку получить нельзя».

# time = int(input("Сколько сейчас время: "))
# if time == 10 or time == 18:
#     print("Посылку можно получить!")
# else:
#     print("Сейчас нельзя получить посылку")