f1 = open("Input/numbers.txt", "r")
data = f1.read()
nums = data.split()

big_num = list(nums)[0]
for num in nums:
    if int(num) > int(big_num):
        big_num = num

f2 = open("Output/output03.txt", "w")
f2.write(str(big_num))