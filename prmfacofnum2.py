import math

def primefactornum(num):
    factors = []
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            factors.append(i)
            while num % i == 0:
                num = num // i
    if num != 1:
        factors.append(num)
    return factors   # 🔹 missing return

num = 28
print(primefactornum(num))

