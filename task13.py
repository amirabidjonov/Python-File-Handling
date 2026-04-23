f1 = open("Input/students.txt", "r")
result = f1.read().split()
sort_students = sorted(result)

f2 = open("Output/output13.txt", "w")
result = f2.write(str(sort_students))