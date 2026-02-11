n=int(input())
for row in range(n):
    #spaces
    for col in range(row):
        print(" ",end="")
        #stars
    for col in range(2*n-2*row-1):
        print("*",end="")
   # for col in range(row):
    #    print(" ",end="")
    print()