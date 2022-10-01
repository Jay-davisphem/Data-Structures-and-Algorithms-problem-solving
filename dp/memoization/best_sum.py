def best_sum(target, list, memo={}):
    if target in memo:
        return memo[target]
    if target == 0:
        return []
    if target < 0:
        return None

    best = None
    for val in list:
        rem = target - val
        res = best_sum(rem, list)
        if res != None:
            comb = res + [val]
            if best == None or len(comb) < len(best):
                best = comb

    memo[target] = best
    return best


print(best_sum(300, [7, 14]))
print(best_sum(60, [3, 10, 60, 30]))
