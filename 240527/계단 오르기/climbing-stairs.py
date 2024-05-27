n = int(input())
dp = [-1 for _ in range(n+1)]


def recur(current):
    if not 0<= current <= n:
        return 0
    if dp[current] != -1:
        return dp[current]    
    if current == 0:
        return 1
    dp[current] = recur(current-2) + recur(current-3)

    return dp[current]
recur(n)
print(dp[n])