def count_construct(target, strings):
    n = len(target)
    list = [1] + [0 for i in range(n)]

    for i in range(n+1):
        if not list[i]:
            continue

        for str in strings:
            ln = len(str)
            if(i + ln <= n and target[i:i + ln] == str):
                list[i + ln] += list[i]
    return list[n]


print(count_construct('purple', ['purp', 'p', 'ur', 'le', 'purpl']))
print(count_construct('abcdef', ['ab', 'abc', 'cd', 'def', 'abcd']))
