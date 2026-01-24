my_dict = { 'tuple': (1, 2, 3, 4, 5),
            'list': [1, 2, 3, 4, 5],
            'dict': {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5},
            'set': {1, 2, 3, 4, 5}}


# Для того что хранится под ключом "кортеж(tuple)" выведите на экран последний элемент
my_tuple = tuple(my_dict['tuple'])
my_list = list(my_dict['list'])
my_set = set(my_dict['set'])
my_dic_new = dict(my_dict['dict'])

print(my_tuple[-1])
#print(my_list)
#print(my_set)
#print(my_dic_new)

# Для того что хранится под ключом list:
#добавьте в конец списка еще один элемент
#удалите второй элемент списка
my_list.append('fifty two')
print(my_list.append('4 four'))
my_list.pop(1)
print(my_list)

# Для того что хранится под ключом dict:
#добавьте элемент с ключом ('i am a tuple') и любым значением
#удалите какой-нибудь элемент
my_dic_new['i am a tuple'] = False
print(my_dic_new)
del my_dic_new['c']
print(my_dic_new)


#Для того что хранится под ключом 'set':
#добавьте новый элемент в множество
#удалите элемент из множества
my_set.add('Porridge')
print(my_set)
my_set.remove(2)
print(my_set)

