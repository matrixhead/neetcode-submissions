class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [] 
        for _ in s:
            dp.append(False)
        dp.append(True)
        for i in range(len(s)-1,-1,-1):
            for word in wordDict:
                matched = True
                for j, c2 in enumerate(word):
                    if (i+j) >= len(s) or c2 != s[i+j] :
                        matched = False
                        break
                if matched:
                    dp[i] = dp[i] or dp[i+len(word)]
                    print(f"{word} matched at {i}")
                    
                
        return dp[0]


        