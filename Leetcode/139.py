from typing import List

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        length = len(s)
        dp = [False] * (length + 1)
        dp[0] = True
        word_set = set(wordDict)
        for end in range(1, length + 1):
            for mid in range(0, end):
                if dp[mid] and s[mid:end] in word_set:
                    dp[end] = True
                    break
        return dp[length]
