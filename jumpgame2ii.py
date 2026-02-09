def jumpgame(arr):
    n = len(arr)
    jumps = 0
    l = 0
    r = 0

    while r < n - 1:
        farthest = 0

        for ind in range(l, r + 1):
            farthest = max(farthest, ind + arr[ind])

        l = r + 1
        r = farthest
        jumps += 1

    return jumps
arr = [2, 3, 1, 1, 4]
print(jumpgame(arr))