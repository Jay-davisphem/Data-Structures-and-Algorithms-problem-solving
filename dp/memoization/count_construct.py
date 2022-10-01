def count_construct(target, wordBank, memo={}):
    if target in memo:
        return memo[target]
    if target == "":
        return 1

    count = 0
    for word in wordBank:
        if target.startswith(word):
            rem = target[len(word) :]
            count += count_construct(rem, wordBank)
    memo[target] = count
    return count


b = (
    "eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef",
    ["e", "ee", "eee", "eeee", "eeeee", "eeeeee"],
)
a = ("purple", ["pur", "ple", "pl", "e", "pu", "r", "purple"])
print(count_construct(*b))
