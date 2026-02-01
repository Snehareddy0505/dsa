def longsubstringoutrepchar(s):
    n = len(s)
    maxlen = 0

    for i in range(n):
        hash = [0] * 256   # to track characters

        for j in range(i, n):
            if hash[ord(s[j])] == 1:
                break

            curr_len = j - i + 1
            maxlen = max(maxlen, curr_len)
            hash[ord(s[j])] = 1

    print(maxlen)
# Example
s = "abcabcbb"
longsubstringoutrepchar(s)
