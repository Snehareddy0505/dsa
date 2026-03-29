#recandmemo
def solve(i, j, s, t, dp):
    if j < 0:
        return 1   # formed t
    if i < 0:
        return 0   # s finished but t not

    if dp[i][j] != -1:
        return dp[i][j]

    if s[i] == t[j]:
        dp[i][j] = solve(i-1, j-1, s, t, dp) + solve(i-1, j, s, t, dp)
    else:
        dp[i][j] = solve(i-1, j, s, t, dp)

    return dp[i][j]


def numDistinct(s, t):
    n, m = len(s), len(t)
    dp = [[-1]*m for _ in range(n)]
    return solve(n-1, m-1, s, t, dp)
#tabulation
def numDistinct(s, t):
    n, m = len(s), len(t)
    dp = [[0]*(m+1) for _ in range(n+1)]

    # Base case
    for i in range(n+1):
        dp[i][0] = 1   # empty t

    for i in range(1, n+1):
        for j in range(1, m+1):
            if s[i-1] == t[j-1]:
                dp[i][j] = dp[i-1][j-1] + dp[i-1][j]
            else:
                dp[i][j] = dp[i-1][j]

    return dp[n][m]
#spaceoptimzation
def numDistinct(s, t):
    n, m = len(s), len(t)
    dp = [0]*(m+1)
    dp[0] = 1

    for i in range(1, n+1):
        # go backwards ⚠️ important
        for j in range(m, 0, -1):
            if s[i-1] == t[j-1]:
                dp[j] = dp[j] + dp[j-1]

    return dp[m]