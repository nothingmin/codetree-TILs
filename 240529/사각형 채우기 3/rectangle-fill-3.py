n = int(input())

dp = [0] * 10001

dp[1] = 2
dp[2] = 7

for i in range(3,n+1):
    dp[i] = (dp[i-1]*2 + dp[i-2]*3)%1_000_000_007
print(dp[n])