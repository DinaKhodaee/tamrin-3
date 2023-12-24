n = int(input("Enter your fav number: "))
for i in range (n):
    if i %2==0:
        print("#", end="")
    else:
        print("*", end="")