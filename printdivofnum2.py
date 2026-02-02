import math

def printdivofnum(num):
    arr = []
    for i in range(1, int(math.sqrt(num)) + 1):
        if num % i == 0:
            arr.append(i)
            if num // i != i:
                arr.append(num // i)
    return sorted(arr)
print(printdivofnum(15))

