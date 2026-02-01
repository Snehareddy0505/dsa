def longsubatmosdistchar(s,k):
    maxlen = 0
    l = 0
    r = 0
    mpp = {}

    while r < len(s):
        # add current character
        mpp[s[r]] = mpp.get(s[r], 0) + 1

        # shrink window if more than k distinct characters
        if len(mpp) > k:
            mpp[s[l]] -= 1
            if mpp[s[l]] == 0:
                del mpp[s[l]]
            l += 1

        # update maximum length
        maxlen = max(maxlen, r - l + 1)
        r += 1

    return maxlen

s = "eceba"
k = 2
print(longsubatmosdistchar(s, k))
