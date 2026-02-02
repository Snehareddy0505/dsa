def numsubstrconallchar(s):
    n = len(s)
    cnt = 0

    for i in range(n):
        hash = [0, 0, 0]   # for 'a', 'b', 'c'
        for j in range(i, n):
            hash[ord(s[j]) - ord('a')] = 1

            if hash[0] + hash[1] + hash[2] == 3:
                cnt += 1

    print(cnt)
s = "abcabc"
numsubstrconallchar(s)
