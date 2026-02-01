def fruitintobas(arr, k):
    l = 0
    maxlen = 0
    mpp = {}   # dictionary to store fruit count

    for r in range(len(arr)):
        # add current fruit to map
        mpp[arr[r]] = mpp.get(arr[r], 0) + 1

        # if more than k fruit types, shrink window
        while len(mpp) > k:
            mpp[arr[l]] -= 1
            if mpp[arr[l]] == 0:
                del mpp[arr[l]]
            l += 1

        # update maximum length
        maxlen = max(maxlen, r - l + 1)

    return maxlen


# Example
arr = [1, 2, 1, 2, 3]
k = 2
print(fruitintobas(arr, k))
