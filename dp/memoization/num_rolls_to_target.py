def dices_sum(n, k, target, memo={}):
    if (n, target) in memo:
        return memo[(n, target)]
    if n == 0:
        return 0 if target > 0 else 1

    ans = 0
    for kk in range(max(0, target - k), target):
        ans += dices_sum(n - 1, k, kk)
    memo[(n, target)] = ans % (10**9 + 7)
    return ans
