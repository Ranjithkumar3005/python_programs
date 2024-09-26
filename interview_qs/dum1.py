def solve(N):
    dp = [0] * (N + 1)
    dp[1] = 1
    print(dp)
    for i in range(1, N + 1):
        for j in range(i * 2, N + 1, i):
            dp[j] += dp[i]

    return dp[N]


print(solve(32454))
