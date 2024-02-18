applicants = int(input('Количество студентов: '))
students = []
count = []

for i in range(applicants):
    i += 1
    num = input(str(i) + '-й студент: ')
    bul = int(input('Балл: '))
    students.append(num)
    count.append(bul)

sums = sum(count)
average_score = round(sums / applicants)

print()
print("Средний балл: ", average_score, '. ', "Студенты с баллом выше среднего:", sep='')

std = {students: count for students, count in zip(students, count)}

for i in students:
    if std[i] >= average_score:
        print(i)
