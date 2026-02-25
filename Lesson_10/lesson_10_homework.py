# 1
#Декоратор должен делать следующее
#распечатывать слово "finished" после выполнения декорированной функции


def decorate(func):
    def wrapper():
        func()
        print(f'Finished {func.__name__}')
    return wrapper

@decorate
def summarising():
    summ = 18 + 3
    print(summ)

summarising()


#
#2
# Создайте универсальный декоратор, который будет управлять тем,
# сколько раз запускается декорируемая функция
# Код, использующий этот декоратор может выглядеть, например, так:

# @repeat_me
# def example(text):
#     print(text)

# example('print me', count=2)
# В результате работы будет такое:

# print me

# print me

def repeat_me_1(func):
    def wrapper(text_to_print, **kwargs):
        for keys, values in kwargs.items():
            values = int(values)
            while True:
                if values > 0:
                    values = values - 1
                    func(text_to_print)
                    print('')
                else:
                    break
    return wrapper


@repeat_me_1
def example(text):
    print(text)

example('print me', count=2)


# создать декоратор, который сможет обработать такой код:

# @repeat_me(count=2)
# def example(text):
#     print(text)

# example('print me')



def repeat_me_2(**kwargs):
     def decorator_2(func):
        def wrapper(text_to_print2):
            for key, value in kwargs.items():
                value = int(value)
                while True:
                     if value > 0:
                        value = value - 1
                        func(text_to_print2)
                        print('')
                     else:
                        break
        return wrapper
     return decorator_2

@repeat_me_2(count=2)
def example_2(text2):
    print(text2)

example_2('print me')

#3
# Задание на декораторы 3
# Напишите программу: Есть функция которая делает одну из арифметических операций с переданными
# ей числами (числа и операция передаются в аргументы функции). Функция выглядит примерно так:

# def calc(first, second, operation):
#     if operation == '+':
#         return first + second
#     elif .....
# Программа спрашивает у пользователя 2 числа (вне функции)

# first = int(input('Введите число: '))
# second = int(input('Введите второе число: '))
# sign = input('Введите знак операции: ')
#
#
# def calc(first_num, second_num, operation):
#     if operation == '+':
#         return first_num + second_num
#     elif operation == '-':
#         return first_num - second_num
#     elif operation == '*':
#         return first_num * second_num
#     elif operation == '/':
#         return first_num / second_num
#
#
# print(calc(first, second, sign))

# Создайте декоратор, который декорирует функцию calc и управляет тем какая операция будет произведена:


def calc_decorator(func):
    def wrapper(num_1, num_2):
        num_1 = int(num_1)
        num_2 = int(num_2)
        if num_1 < 0 or num_2 <0:
            return func(num_1, num_2, '*')
        elif num_1 > num_2:
            return func(num_1, num_2, '-')
        elif num_2 > num_1:
            return func(num_1, num_2, '/')
        elif num_1 == num_2:
            return func(num_1, num_2, '+')
    return wrapper

first = int(input('Введите число: '))
second = int(input('Введите второе число: '))
#sign = input('Введите знак операции: ')

@calc_decorator
def calc(first_num, second_num, operation):
    if operation == '+':
        return first_num + second_num
    elif operation == '-':
        return first_num - second_num
    elif operation == '*':
        return first_num * second_num
    elif operation == '/':
        return first_num / second_num

print(calc(first, second))


# если числа равны, то функция calc вызывается с операцией сложения этих чисел
# если первое больше второго, то происходит вычитание второго из певрого
# если второе больше первого - деление первого на второе
# если одно из чисел отрицательное - умножение

#          first = int(input('Введите первое число: '))
#          second = int(input('Введите второе число: '))
#          operation = input('Введите арифимитечкий оператор: ')


#4
# Задание на List comprehension
# Дан такой кусок прайс листа:

# (Копируйте эту переменную (константу) в код прямо как есть)

# При помощи list comprehension и/или dict comprehension превратите этот текст в словарь такого вида:

# {'тетрадь': 50, 'книга': 200, 'ручка': 100, 'карандаш': 70, 'альбом': 120, 'пенал': 300, 'рюкзак': 500}
# В выполнении не должно быть циклов.

# Обратите внимание, что цены в словаре имеют тип int (они не в кавычках)

PRICE_LIST = '''тетрадь 50р
книга 200р
ручка 100р
карандаш 70р
альбом 120р
пенал 300р
рюкзак 500р'''



dictionary_1 = PRICE_LIST.split('\n')


print(dictionary_1)
new_dict = {x.split()[0]: int(x.split()[1].strip('р')) for x in dictionary_1}
print(new_dict)






