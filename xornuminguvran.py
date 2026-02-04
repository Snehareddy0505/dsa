def xornumofguvennum(n):
    ans = 0
    for i in range(1, n + 1):
        ans ^= i
    return ans

n = 4
print(xornumofguvennum(n))
