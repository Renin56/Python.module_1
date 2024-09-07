#Вводные данные
grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
print('Оценки студентов: ',  grades)
#print('Неупорядоченный список студентов:', students)

# считаем средний бал
aaron = sum(grades[0]) / len(grades[0])
bilbo = sum(grades[1]) / len(grades[1])
johnny = sum(grades[2]) / len(grades[2])
khendrik = sum(grades[3]) / len(grades[3])
steve = sum(grades[4]) / len(grades[4])

#сортируем множество и преобразовываем в список
stud = list(sorted(students))
print('Упорядоченный список студентов:', stud)

#формируем словарь
average_score = {stud[0]: aaron, stud[1]: bilbo, stud[2]: johnny, stud[3]: khendrik, stud[4]: steve}
print('Средний бал студентов:'.upper())
print(average_score)
