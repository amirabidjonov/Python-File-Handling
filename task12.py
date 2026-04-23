f1 = open("Input/students.txt", "r")
result = f1.read().split()
len_students = len(result)

f2 = open("Output/output12.txt", "w")
result = f2.write(str(len_students))