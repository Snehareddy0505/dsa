def sumofnnum(i, total):
    if i == 0:
        print(total)
        return
    sumofnnum(i - 1, total + i)

n = int(input("Enter n: "))
sumofnnum(n, 0)
