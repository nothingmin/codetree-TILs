n = int(input())
dp = [-1 for _ in range(n + 1)]
dp[0] = 0
dp[1] = 1
dp[2] = 3

for i in range(3, n + 1):
    dp[i] = (dp[i - 1] + dp[i - 2] * 2)%10007

print(dp[n-2])