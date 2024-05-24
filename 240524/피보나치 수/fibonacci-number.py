n = int(input())
#
# dp = [-1 for _ in range(n + 1)]
#
# dp[0] = 1
# dp[1] = 1
# for i in range(2, n + 1):
#     dp[i] = dp[i - 1] + dp[i - 2]
# print(dp[n - 1])


def recur(index):
    if index == 1 or index == 0:
        return 1


    return recur(index - 1) + recur(index - 2)

print(recur(n-1))