immutable_var = (1, 2, 'слово', True, [3, 4, 5])
print('Кортеж - неизменяемый список')
print(immutable_var)

# элементы кортежа изменить нельзя (кроме элемента являющийся списком). кортеж относится к неизменяемым спискам
# immutable_var[0] = '7'
# print(immutable_var)

mutable_list = [1, 2, 3, 4, 5]
print('Изменяемый список')
print(mutable_list)
mutable_list[0] = 6
mutable_list[2] = 'hi'
mutable_list[4] = True
print(mutable_list)