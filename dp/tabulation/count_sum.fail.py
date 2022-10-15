def count_sum(target, array):
    dp = [None] * (target + 1)
    dp[0] = []

    count = 0
    for i in range(0, len(dp)):
        if dp[i] is not None:
            for num in array:
                if i + num <= target:
                    new = [get for get in dp[i]] + [num]
                    if sum(new) == target:
                        count += 1
                    dp[i + num] = new
    return count


print(count_sum(9, [1, 2, 3, 4, 5]))
