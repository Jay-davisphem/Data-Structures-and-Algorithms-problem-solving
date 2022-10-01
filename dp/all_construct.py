def all_construct(target, wordBank, memo={}):
    if target in memo:
        return memo[target]
    if target == "":
        return [[]]

    combinations = []
    for word in wordBank:
        n = len(word)
        if target.startswith(word):
            end = target[n:]
            end_ways = all_construct(end, wordBank)
            target_ways = list(map(lambda way: [word] + way, end_ways))
            print(target_ways)
            for target_way in target_ways:
                combinations.append(target_way)
    memo[target] = combinations
    return combinations


b = (
    "eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef",
    ["e", "ee", "eee", "eeee", "eeeee", "eeeeee"],
)
a = ("purple", ["pur", "ple", "pl", "e", "pu", "r", "purple", "r"])
print(all_construct(*b))
