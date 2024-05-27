n = int(input())
dp = [-1 for _ in range(1001)]
dp[2] = 1
dp[3] = 1
def recur(current):
    if not(0 <= current <= n):
        return 0
    if dp[current] != -1:
        return dp[current]    
    dp[current] = (recur(current-2) + recur(current-3))%10007
    return dp[current]
recur(n)
print(dp[n])