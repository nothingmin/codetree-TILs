n = int(input())


#
dp = [-1 for _ in range(n + 1)]
dp[0] = 1
dp[1] = 1

def recur(index):
    if dp[index] != -1:
        return dp[index]
    if index == 1 or index == 0:
        return 1

    dp[index] = recur(index - 1) + recur(index - 2)
    return dp[index]

print(recur(n - 1))