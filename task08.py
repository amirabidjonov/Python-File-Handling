f01 = open("Input/numbers.txt", "r")
result = f01.read()
list_nums = list(result.split())

sonlar = 0
for num in list_nums:
    if int(num) % 5 != 0:
        sonlar += int(num)

f2 = open("Output/output08.txt", "w")
f2.write(str(sonlar))