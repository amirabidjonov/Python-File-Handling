f1 = open("Input/students.txt", "r")
result = list(f1.read().split())

total_len = 0
for num in result:
    total_len += len(num)

f2 = open("Output/output15.txt", "w")
f2.write(str(total_len))