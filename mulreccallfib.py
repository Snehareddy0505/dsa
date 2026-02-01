def fibomul(n):
    if n <= 1:
        return n
    last = fibomul(n - 1)
    slast = fibomul(n - 2)
    return last + slast

n = int(input())
print(fibomul(n))
