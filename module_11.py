# import math

# TODO: Модуль 11. Структуры данных Python и ООП

# Функция Range
# Range - это функция-генератор списка чисел в указанном диапазоне
# range по сути можно трактовать как диапазон. Применяется, когда нам нужно ограничить выполнения программы, цикла в
# определенных границах

americano = "americano"
raf = "raf"

def coffee_machine(type, ml):
    if type == americano or type == raf:
        if type == americano:
            for ml in range(400, 500):
                print(f"Приготовление кофе: {type}\n с объемом {ml}мл")
        else:
            print(f"Приготовление кофе: {type}\n с объемом {ml}мл")
    else:
        print("Некорректно выбран вид кофе!")

# coffee_machine(americano, 400)

# Работа с файлами (в системе)
def read_users():
    with open('files/users.txt', "r") as file:      # read
        content = file.read()   # Прочитает весь файл
        print(content)

# read_users()

def rewrite_users():
    with open('files/users.txt', "w") as file:  # write
        new_user = "alexey ivanov"
        file.write(new_user)  # Перезапишет все данные в файле!

# rewrite_users()

def add_users():
    adding_user = "Alex Novoselov"
    with open('files/users.txt', "a") as file:      # append
        file.write(f"\n{adding_user}")     # Добавляет новую строку в конец файла, не заменяя их полностью

# add_users()

# TODO: Работа с модулями (в проекте)
# Модуль – это любой файл, который хранит в себе какие-либо функции, классы или еще что-либо.
# Он содержит определенные инструкции, написанные на языке Python.

# DRY
from module_10 import show_time     # Импортируем функцию показать время из 10 модуля
# from module_10 import *

now = "Текущее время:"

# print(now, show_time())     # используем функцию по ее названию
# print(math.fabs(10))


# Функция Return - можно перевести как "вернуть"
# Используется либо для возврата какого-либо значения после выполнения функции, либо для возврата пустого значения
def check_postive(number):
    if number >= 0:
        return "Число положительное"
    else:
        return "Число отрицательное"

# print(check_postive(5))

def divide(x, y):
    return x / y
    # print(x / y)

# print(int(divide(12, 3)))
# divide(12, 3)


# Работа с исключениями. Конструкция Try&Except
# Используется для обработки ошибок (исключений) при выполнении программного кода
# Если в блоке try возникает ошибка, тогда программа не "падает", а перейдет в блок except где можно дать подсказку
# в чем проблема и как ее решить
import requests

def download_data(url):
    try:        # Функция "попытается" выполнить код, но если произойдет ошибка, то выполнит логику except
        response = requests.get(url)
        response.raise_for_status() # Генерирует ошибку, если код ответа не 200
        return response.text
    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP ошибка: {http_err}")
    except Exception as err:
        print(f"Неизвестная ошибка: {err}")

my_url = "https://urban-university.ru/members/courses/course825686491042/20241122-0000lekcia-rabota-s-iskluceniami-konstrukcia-tryampexcept-830427872941"
fake_url = 123125
# print(download_data(fake_url))


# Создание и наследование классов
# Класс — это шаблон для создания объектов. Он определяет, какие атрибуты (данные) и методы (функции) будут у
# создаваемых объектов. В нашем случае мы создадим класс для работы с алфавитами различных языков.

class Car:  # объявляем класс Машины
    # color = "Красный"
    def __init__(self, name, year, model, color):    # здесь указываем инициализацию класса (какие параметры класс будет содержать)
        self.year = year
        self.model = model
        self.color = color
        self.name = name

    # def car_description(self):      # пишем дополнительную функцию, которая нам возвращает текстовую информацию о машинах
    #     car_info = f"Авто:{self.name}\nГод выпуска: {self.year}\nМодель: {self.model}\n{self.color}"
    #     return car_info

uaz = Car("УАЗ", 2010, "Патриот", "Черный")        # создаем экземпляр класса Машины, указываем конкретно год выпуска и модель
bmw = Car("BMW", 2020, "E3", "Синий")

# print(uaz.car_description())      # выводим на печать данные об автомобиле (экземпляр класса) с использованием доп функции
# print(bmw.car_description())
# print(f"Год выпуска: {uaz.year}\nМодель: {uaz.model}")  # Как бы выглядел вывод на печать без функции car_description

