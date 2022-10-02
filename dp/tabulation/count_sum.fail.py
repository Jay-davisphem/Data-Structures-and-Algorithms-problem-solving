def count_sum(target, array):
    dp = [None] * (target + 1)
    dp[0] = []

    for i in range(0, len(dp)):
        if dp[i] is not None:
            for num in array:
                if i + num <= target:
                    new = [get for get in dp[i]] + [num]
                    old = dp[i + num]
                    if old == []:
                        dp[i + num] = new
                    elif old is None:
                        dp[i + num] = [new]
                    else:
                        dp[i + num] = [get for get in old] + new
    return dp[target]


print(count_sum(9, [5, 3, 4, 2]))
