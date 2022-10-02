def how_sum(target, array):
    dp = [None] * (target + 1)
    dp[0] = []
    for i in range(0, len(dp)):
        if dp[i] is not None:
            for num in array:
                if i + num <= target:
                    dp[i + num] = [get for get in dp[i]] + [num]
    return dp[target]


print(how_sum(700, [5, 3, 4]))
