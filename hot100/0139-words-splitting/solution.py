class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = {} # 我这里想用dp[i]代表s[0:i]是否可以被拆分。
        dp[0] = True
        max_len = min_len = len(wordDict[0])
        for word in wordDict:
            if len(word) > max_len:
                max_len = len(word)

        for i in range(1,len(s)+1):
            dp[i] = False        
            for j in range(max(i - max_len, 0), i):
                dp[i] = (dp[j] and (s[j:i] in wordDict))
                if dp[i] == True:
                    break
        return dp[len(s)]
            

        
