def atMostK(arr, k):
    l = 0
    cnt = 0
    mpp = {}

    for r in range(len(arr)):
        mpp[arr[r]] = mpp.get(arr[r], 0) + 1

        while len(mpp) > k:
            mpp[arr[l]] -= 1
            if mpp[arr[l]] == 0:
                del mpp[arr[l]]
            l += 1

        cnt += (r - l + 1)

    return cnt
arr = [1,2,1]
k = 2
print(atMostK(arr,k))