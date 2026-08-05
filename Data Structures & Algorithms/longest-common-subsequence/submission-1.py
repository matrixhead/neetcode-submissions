class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        t1len = len(text1)
        t2len = len(text2)
        dp = [[0 for _ in range(t2len)] for _ in range(t1len)]

        for i in range(t1len):
            for j in range(t2len):
                matched = 0
                if text1[i] == text2[j]:
                    matched = 1

                if i == 0 and j==0:
                    dp[i][j] = matched
                elif i == 0:
                    if matched == 1:
                        dp[i][j] = matched
                    else:
                        dp[i][j] = dp[i][j-1] + matched
                elif j == 0:
                    if matched == 1:
                        dp[i][j] = matched
                    else:
                        dp[i][j] = dp[i-1][j] + matched
                else:
                    if matched == 1:
                        dp[i][j] = dp[i-1][j-1] + matched
                    else:
                        dp[i][j] = max(dp[i-1][j],dp[i][j-1])
                
        
        return dp[t1len-1][t2len-1] 

        