f1 = open("Input/numbers.txt", "r")
data = f1.read()
list_nums = list(data.split())


toq = []
for num in list_nums:
    if not int(num) % 2 == 0:
        toq.append(num)

f2 = open("Output/output06.txt", "w")
f2.write(str(toq))