# программа для добавления ing в конец каждого слова
#
# Условия работы программы:
# знаки препинания не пишутся внутри слов
# если идет запятая или точка после слова, то знак идет после ing


my_string = ("Etiam tincidunt neque erat, quis molestie enim imperdiet vel. "
             "integer urna nisl, facilisis vitae semper at, gignissim vitae libero")

text_string = my_string.split()
print(my_string)

# for each_word in text_string:
#     if ',' in each_word:
#         print(each_word.replace(',','ing,'), end = ' ')
#     elif '.' in each_word:
#         print(each_word.replace('.', 'ing.'), end = ' ')
#     else:
#         print(f'{each_word}ing', end = ' ')

new_string = []
for each_word in text_string:
    if ',' in each_word:
       new_string.append(each_word.replace(',','ing,'))
    elif '.' in each_word:
        new_string.append(each_word.replace('.', 'ing.'))
    else:
        new_string.append(each_word + 'ing')

print(' '.join(new_string))




# Программа для перебора последовательности от 1 до 100
# УСЛОВИЯ ДЛЯ РАБОТЫ ПРОГРАММЫж
# ДЛЯ КРАТНЫХ 3 ДОЛЖНА ПИСАТЬ "FUZZ" вместо числа
# для кратных 5 должна писать "BUZZ" вместо числа
# для кратных 3 и 5 должна писать "FUZZBUZZ" вместо числа
# иначе должна писать само число

incomming_numbers = range(1,101)
result = []
for any_number in incomming_numbers:
    if (any_number % 5) ==0 and (any_number % 3) ==0:
        result.append('FUZZBUZZ')
    elif (any_number % 5) != 0 and (any_number % 3) != 0:
        result.append(any_number)
    elif (any_number % 3) == 0:
        result.append('FUZZ')
    elif (any_number % 5) == 0:
        result.append('BUZZ')
print(result)


