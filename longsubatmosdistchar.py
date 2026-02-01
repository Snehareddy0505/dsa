def longsubatmokdistchar(s, k):
    maxlen = 0
    n = len(s)

    for i in range(n):
        mpp = {}
        for j in range(i, n):
            mpp[s[j]] = mpp.get(s[j], 0) + 1

            if len(mpp) <= k:
                maxlen = max(maxlen, j - i + 1)
            else:
                break

    return maxlen
s = "eceba"
k = 2
print(longsubatmokdistchar(s,k))