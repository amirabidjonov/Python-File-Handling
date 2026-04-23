f1 = open("Input/numbers.txt", "r")
data = f1.read()
list_nums = list(data.split())


sonlar = []
for num in list_nums:
    sonlar.append(int(num) ** 2)

f2 = open("Output/output07.txt", "w")
f2.write(str(sonlar))