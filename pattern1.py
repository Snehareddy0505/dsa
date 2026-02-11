n=int(input())
for row in range(n):
    for col in range(n-row-1):
        print(" ",end="")
    for col in range(row+1):
        print("*",end="")
   # for col in range(row-n-1):
    # print(" ",end=" ")
    print()