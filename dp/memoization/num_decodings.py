from typing import List


class Solution:
    def num_decodings(
        self, s: str, ways: List[str] = [str(i) for i in range(1, 27)], memo={}
    ) -> int:
        if s in memo:
            return memo[s]
        if s == "":
            return 1

        count = 0
        for ss in ways:
            if s.startswith(ss):
                end = s[len(ss) :]
                count += self.num_decodings(end, ways)
        memo[s] = count
        return count


sol = Solution()
print(sol.num_decodings("226"))
