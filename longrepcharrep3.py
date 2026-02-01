def longrepcharrep(s, k):
    l = 0
    maxlen = 0
    maxf = 0
    freq = [0] * 26

    r = 0
    while r < len(s):
        idx = ord(s[r]) - ord('A')
        freq[idx] += 1

        maxf = max(maxf, freq[idx])

        if (r - l + 1) - maxf > k:
            freq[ord(s[l]) - ord('A')] -= 1
            l += 1

        maxlen = max(maxlen, r - l + 1)
        r += 1

    print(maxlen)
s = "AABABBA"
k = 1
longrepcharrep(s, k)

