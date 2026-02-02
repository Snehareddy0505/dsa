def permutation(ds, used, n):
    if len(ds) == n:
        print(ds)
        return

    for i in range(1, n + 1):
        if not used[i]:
            ds.append(i)
            used[i] = True

            permutation(ds, used, n)

            # backtrack
            ds.pop()
            used[i] = False


n = 3
used = [False] * (n + 1)
permutation([], used, n)
