# Задание "Средний балл":
# Вам необходимо решить задачу из реальной жизни: "школьные учителя устали подсчитывать вручную средний балл каждого ученика,
# поэтому вам предстоит автоматизировать этот процесс":
#
# На вход даны следующие данные:
#
#     Список: grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
#     Множество: students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
#
# Список grades содержит списки оценок для каждого ученика в алфавитном порядке.
# Множество students содержит неупорядоченную последовательность имён всех учеников в классе.
# Напишите программу, которая составляет словарь, используя grades и students, где ключом будет имя ученика, а значением - его средний балл.

grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}

#1. отсортируем студентов
students_list = list(students)
students_list.sort()
print(students_list)

#2. так как циклы еще не проходили, вроде как остается добавление только перечислением
average_grades = dict()
average_grades[students_list[0]] = sum(grades[0]) / len(grades[0])
average_grades[students_list[1]] = sum(grades[1]) / len(grades[1])
average_grades[students_list[2]] = sum(grades[2]) / len(grades[2])
average_grades[students_list[3]] = sum(grades[3]) / len(grades[3])
average_grades[students_list[4]] = sum(grades[4]) / len(grades[4])
print(average_grades)
