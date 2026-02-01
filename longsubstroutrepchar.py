def longsubstroutrepchar(s):
    n = len(s)
    maxlen = 0

    # stores last index of each character
    hash = [-1] * 256

    l = 0
    for r in range(n):
        if hash[ord(s[r])] >= l:
            l = hash[ord(s[r])] + 1

        hash[ord(s[r])] = r
        curr_len = r - l + 1
        maxlen = max(maxlen, curr_len)

    print(maxlen)
s = "abcabcbb"
longsubstroutrepchar(s)
