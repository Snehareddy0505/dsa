def miniwinsubstr(s, t):
    if not s or not t:
        return ""

    freq = {}
    for ch in t:
        freq[ch] = freq.get(ch, 0) + 1

    l = 0
    cnt = 0
    minlen = float('inf')
    start = 0

    for r in range(len(s)):
        if s[r] in freq:
            freq[s[r]] -= 1
            if freq[s[r]] >= 0:
                cnt += 1

        while cnt == len(t):
            if (r - l + 1) < minlen:
                minlen = r - l + 1
                start = l

            if s[l] in freq:
                freq[s[l]] += 1
                if freq[s[l]] > 0:
                    cnt -= 1
            l += 1

    return "" if minlen == float('inf') else s[start:start+minlen]
s = "ADOBECODEBANC" 
t = "ABC"
print(miniwinsubstr(s,t))