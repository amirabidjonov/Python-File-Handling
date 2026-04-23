f01 = open("Input/numbers.txt", "r")
result = f01.read()
list_nums = list(result.split())

result = sorted(list_nums)

f2 = open("Output/output10.txt", "w")
f2.write(str(result))