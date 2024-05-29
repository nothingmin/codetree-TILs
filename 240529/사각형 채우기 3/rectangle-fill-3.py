n = int(input())

dp = [0] * 10001

dp[1] = 2
dp[2] = 7
dp[3] = 22
for i in range(4,n+1):
    dp[i] = (dp[i-1]*2 + dp[i-2]*3+dp[i-3]*2)%1000000007
print(dp[n])