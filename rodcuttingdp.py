#recmemorization
def solve(i, n, price, dp):
    if i == 0:
        return n * price[0]

    if dp[i][n] != -1:
        return dp[i][n]

    not_take = solve(i-1, n, price, dp)

    take = float('-inf')
    rod_len = i + 1
    if rod_len <= n:
        take = price[i] + solve(i, n - rod_len, price, dp)

    dp[i][n] = max(take, not_take)
    return dp[i][n]


def cutRod(price, n):
    dp = [[-1]*(n+1) for _ in range(n)]
    return solve(n-1, n, price, dp)
#tabulation
def cutRod(price, n):
    dp = [[0]*(n+1) for _ in range(n)]

    # Base case
    for length in range(n+1):
        dp[0][length] = length * price[0]

    for i in range(1, n):
        for length in range(n+1):
            not_take = dp[i-1][length]

            take = float('-inf')
            rod_len = i + 1
            if rod_len <= length:
                take = price[i] + dp[i][length - rod_len]

            dp[i][length] = max(take, not_take)

    return dp[n-1][n]
#spaceoptimized
def cutRod(price, n):
    dp = [0]*(n+1)

    for i in range(n):
        rod_len = i + 1
        for length in range(rod_len, n+1):
            dp[length] = max(dp[length],
                             price[i] + dp[length - rod_len])

    return dp[n]