f1 = open("Input/students.txt", "r")
result = list(f1.read().split())

name = str(input("name: "))
students = []
for student in result:
    if student.lower() == name.lower():
        students.append(student)
        print("found")
    else:
        print("not found")
f2 = open("Output/output18.txt", "w")
f2.write(str(students))