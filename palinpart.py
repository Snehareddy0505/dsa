def palindromepartition(s, ind, path, res):
    if ind == len(s):
        res.append(path.copy())
        return

    for i in range(ind, len(s)):
        # check if substring s[ind:i+1] is palindrome
        if s[ind:i+1] == s[ind:i+1][::-1]:
            path.append(s[ind:i+1])          # choose
            palindromepartition(s, i+1, path, res)  # explore
            path.pop()                        # backtrack
s = "aab"
res = []
palindromepartition(s, 0, [], res)
print(res)
