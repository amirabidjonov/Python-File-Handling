f1 = open("Input/numbers.txt", "r")
data = f1.read()
list_nums = list(data.split())


juft = []
for num in list_nums:
    if int(num) % 2 == 0:
        juft.append(num)

f2 = open("Output/output04.txt", "w")
f2.write(str(juft))