def can_sum(target, arrays):
    dp = [False] * (target + 1)

    dp[0] = True
    for i in range(0, len(dp)):
        if dp[i]:
            for j in arrays:
                if i + j <= target:
                    dp[i + j] = True
        print(dp)
    return dp[target]


print(can_sum(300, [7, 14]))
