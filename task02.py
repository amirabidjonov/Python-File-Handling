f1 = open("Input/numbers.txt", "r")
data = f1.read()
nums = data.split()

s = 0
for num in nums:
    s += int(num)
    
f2 = open("Output/output02.txt", "w")
f2.write(str(s))