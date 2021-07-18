import random
courses = ['C', 'C++', 'Java']
courses.append('Python')
courses.append('Ab Intio')
print(courses)
courses.remove('C++')
# del courses[1]

if 'C++' in courses:
    print("True")
else:
    print("False")

for course in courses:
    print(course)

sum = 0
for n in [10, 30, 40, 50]:
    sum = sum + n
print("You spent $", sum, " On lunch this week", sep="")

expenses = []
total = 0
for i in range(0, 7, 1):
    expenses.append(float(input("Expense for day: ")))
print(expenses)

for x in expenses:
    total = total + x
print(total)
