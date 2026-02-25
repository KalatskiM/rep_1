person = ['John', 'Doe', 'New York', '+1372829383739', 'US']

# 1. Распаковка списка person в переменные:

name, last_name, city, phone_number, country = person
print(country, name, last_name, city, phone_number, country)


# 2. Получить число из строки с помощью срезов и метода индекс
test_str_1 = 'Результат операции: 42'
test_str_2 = 'результат операции: 514'
test_str_3 = 'результат работы программы: 9'

number_1 = test_str_1.index(':') + 2
number_2 = test_str_2.index(':') + 2
number_3 = test_str_3.index(':') + 2

print((int(test_str_1[number_1:]) + 10), (int(test_str_2[number_2:])+10),  (int(test_str_3[number_3:]))+10)

# 3. Количество учеников изучают эти предметы

students = ['Ivanov', 'Petrov', 'Sidorov']
subjects = ['math', 'biology', 'geography']


print(f'There are students', ', '.join(students), 'who study', ', '.join(subjects))