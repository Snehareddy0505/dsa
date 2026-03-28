#memoandrec
def solve(i, amount, coins, dp):
    if amount == 0:
        return 1
    if i == 0:
        if amount % coins[0] == 0:
            return 1
        return 0

    if dp[i][amount] != -1:
        return dp[i][amount]

    not_take = solve(i-1, amount, coins, dp)

    take = 0
    if coins[i] <= amount:
        take = solve(i, amount - coins[i], coins, dp)

    dp[i][amount] = take + not_take
    return dp[i][amount]


def change(amount, coins):
    n = len(coins)
    dp = [[-1]*(amount+1) for _ in range(n)]
    return solve(n-1, amount, coins, dp)
#tab
def change(amount, coins):
    n = len(coins)
    dp = [[0]*(amount+1) for _ in range(n)]

    # Base case
    for t in range(amount+1):
        if t % coins[0] == 0:
            dp[0][t] = 1

    for i in range(1, n):
        for t in range(amount+1):
            not_take = dp[i-1][t]

            take = 0
            if coins[i] <= t:
                take = dp[i][t - coins[i]]

            dp[i][t] = take + not_take

    return dp[n-1][amount]
#space optimized
def change(amount, coins):
    dp = [0] * (amount + 1)
    dp[0] = 1   # one way to make 0

    for coin in coins:
        for t in range(coin, amount + 1):
            dp[t] += dp[t - coin]

    return dp[amount]