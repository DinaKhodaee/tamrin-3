import random
n = int(input("Enter the number of numbers: "))
num = [random.randint(0,20)]
for i in range(n):
    x = random.randint(0,20)
    if x!=num:
        num.append(x)
print("Your random array:", num)