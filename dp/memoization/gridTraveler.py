def grid_traveler(n, m, memo={}):
    key = f"{n},{m}"  # if n > m else f"{m},{n}"
    if key in memo:
        return memo[key]
    if n == 1 and m == 1:
        return 1
    if n == 0 or m == 0:
        return 0
    memo[key] = grid_traveler(n - 1, m) + grid_traveler(n, m - 1)
    return memo[key]


print(grid_traveler(300, 300))
