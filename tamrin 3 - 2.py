r = []
nr = int(input("How many numbers do you have in your array? "))
for i in range (nr):
    ar =  int(input("Enter your array numbers: "))
    r.append(ar)
for i in range (1,len(r)):
    if r[i] > r[i - 1]:
        print("Correct!")
    else:
        print("Nope!")