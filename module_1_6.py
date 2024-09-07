# списки

my_dict = {'Oleg': 2000, 'Maxim': 1980, 'Petr': 2015, 'Aristarh': 1967}
print(my_dict)
print(my_dict.get('Petr'))
print(my_dict.get('Ivan'))
my_dict.update({'Sergey': 1988, 'Dmitriy': 1994})
print(my_dict)
value = my_dict.pop('Maxim')
print(my_dict)
print(value)


# множества

my_set = {1, 2, True, ('Первый, Второй'), 1, True}
print(my_set)
my_set.add(5)
my_set.add(('Третий, Четвертый'))
print(my_set)
my_set.discard(1)
print(my_set)
