def subarrwithkdiffint(arr, k):
    cnt = 0
    n = len(arr)

    for i in range(n):
        mpp = {}   # dictionary to store frequency
        for j in range(i, n):
            mpp[arr[j]] = mpp.get(arr[j], 0) + 1

            if len(mpp) == k:
                cnt += 1
            elif len(mpp) > k:
                break

    return cnt
arr = [1,2,1,2,3]
k = 2
print(subarrwithkdiffint(arr, k))
