def f(l, r):
    if l >= r:
        return
    a[l], a[r] = a[r], a[l]   # swap
    f(l + 1, r - 1)          # recursive call


# -------- MAIN PART --------
a = list(map(int, input().split()))
n = len(a)

f(0, n - 1)
print(a)
