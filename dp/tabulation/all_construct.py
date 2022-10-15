def all_construct(target, strings):
    n = len(target)
    grid = [[[]]] + [[] for i in range(n)]

    for i in range(n + 1):
        if not grid[i]:
            continue
        for str in strings:
            ln = len(str)
            if(i + ln <= n and target[i: i + ln] == str):
                for j in range(len(grid[i+ln])):
                    grid[i + ln][j].append(str)
    return grid


print(all_construct('purple', ['purp', 'p', 'ur', 'le', 'purpl']))
print(all_construct('abcdef', ['ab', 'abc', 'cd', 'def', 'abcd']))
