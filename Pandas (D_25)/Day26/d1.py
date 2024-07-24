import random

numbers =  [1,1,2,3,5,8,13,21,34,55]
n = [n**2 for n in numbers]
print(n)

names = ['Alex', 'Beth', 'Caroline']
students_scores = {student:random.randint(1,100) for student in names}
print(students_scores)

passed_students = {student:score for (student,score) in students_scores.items() if score >= 60}

print(passed_students)