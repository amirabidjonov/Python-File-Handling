f1 = open("Input/numbers.txt", "r")
data = f1.read()
list_nums = list(data.split())

add_num = 0
for num in list_nums:
    add_num += int(num)

result = add_num / len(list_nums)

f2 = open("Output/output05.txt", "w")
f2.write(str(result))