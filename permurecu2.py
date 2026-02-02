def permutation2(ind, arr):
    if ind == len(arr):
        print(arr)
        return

    for i in range(ind, len(arr)):
        arr[ind], arr[i] = arr[i], arr[ind]   # swap
        permutation2(ind + 1, arr)
        arr[ind], arr[i] = arr[i], arr[ind]   # backtrack


arr = [1, 2, 3]
permutation2(0, arr)
