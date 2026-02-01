def longrepcharreplace(s, k):
    n = len(s)
    maxlen = 0

    for i in range(n):
        freq = [0] * 26   # frequency of characters
        maxf = 0

        for j in range(i, n):
            index = ord(s[j]) - ord('A')
            freq[index] += 1

            maxf = max(maxf, freq[index])

            changes = (j - i + 1) - maxf

            if changes <= k:
                maxlen = max(maxlen, j - i + 1)
            else:
                break

    print(maxlen)
s = "AABABBA"
k = 1
longrepcharreplace(s, k)
