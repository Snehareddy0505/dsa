#recandmemo
def solve(i, j, s1, s2, dp):
    if i < 0 or j < 0:
        return 0

    if dp[i][j] != -1:
        return dp[i][j]

    if s1[i] == s2[j]:
        dp[i][j] = 1 + solve(i-1, j-1, s1, s2, dp)
    else:
        dp[i][j] = max(
            solve(i-1, j, s1, s2, dp),
            solve(i, j-1, s1, s2, dp)
        )

    return dp[i][j]


def lcs(s1, s2):
    n, m = len(s1), len(s2)
    dp = [[-1]*m for _ in range(n)]
    return solve(n-1, m-1, s1, s2, dp)
#tabulation 
def lcs(s1, s2):
    n, m = len(s1), len(s2)
    dp = [[0]*(m+1) for _ in range(n+1)]

    for i in range(1, n+1):
        for j in range(1, m+1):
            if s1[i-1] == s2[j-1]:
                dp[i][j] = 1 + dp[i-1][j-1]
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])

    return dp[n][m]
#spaceoptimization
def lcs(s1, s2):
    n, m = len(s1), len(s2)
    prev = [0]*(m+1)

    for i in range(1, n+1):
        curr = [0]*(m+1)
        for j in range(1, m+1):
            if s1[i-1] == s2[j-1]:
                curr[j] = 1 + prev[j-1]
            else:
                curr[j] = max(prev[j], curr[j-1])
        prev = curr

    return prev[m]