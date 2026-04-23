f01 = open("Input/numbers.txt", "r")
result = f01.read()
list_nums = list(result.split())

sonlar = []
for num in list_nums:
    if len(num) == 1:
        sonlar.append(f"1 xonali: {num}")
    elif len(num) == 2:
        sonlar.append(f"2 xonali: {num}")
    if len(num) == 3:
        sonlar.append(f"3 xonali: {num}")

f2 = open("Output/output09.txt", "w")
f2.write(str(sonlar))