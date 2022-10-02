def how_sum(target: int, list: list, memo={}) -> list:
    if target in memo:
        return memo[target]
    if target == 0:
        return []
    if target < 0:
        return None
    for val in list:
        rem = target - val
        res = how_sum(rem, list, memo)
        if res != None:
            memo[target] = res + [val]
            return memo[target]
    memo[target] = None
    return None


print(how_sum(300, [7, 14, 2]))
