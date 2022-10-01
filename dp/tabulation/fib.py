def fib(n):
    if n < 0:
        return n
    table = [0] * (n + 1)
    table[1] = 1

    for i in range(n + 1):
        if i <= n - 2:
            table[i + 2] += table[i]
        if i <= n - 1:
            table[i + 1] += table[i]
    return table[n]


print(fib(500000))
