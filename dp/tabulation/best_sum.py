def best_sum(target, array):
    dp = [None] * (target + 1)
    dp[0] = []

    for i in range(0, len(dp)):
        if dp[i] is not None:
            for num in array:
                if i + num <= target:
                    new = [get for get in dp[i]] + [num]
                    old = dp[i + num]
                    if old is None:
                        dp[i + num] = new
                    else:
                        dp[i + num] = max(old, new, key=lambda arr: -len(arr))
    return dp[target]


print(best_sum(7, [5, 3, 4, 2]))
