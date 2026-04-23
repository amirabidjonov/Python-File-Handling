f1 = open("Input/students.txt", "r")
result = list(f1.read().split())

students = []
for num in result:
    if len(num) > 5:
        students.append(num)

f2 = open("Output/output16.txt", "w")
f2.write(str(students))