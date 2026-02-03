def sumnum(n):
    if n == 0:        # base condition
        return 0
    return n + sumnum(n - 1)


# -------- MAIN PART --------
n = 5
print(sumnum(n))
