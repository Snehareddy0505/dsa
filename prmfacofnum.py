def prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


def primefactorofnum(num):
    factors = []
    for i in range(2, num + 1):
        if num % i == 0:
            if prime(i):
                factors.append(i)
    return factors
num = 28
print(primefactorofnum(num))
