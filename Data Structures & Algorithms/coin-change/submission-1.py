class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = []
        dp.append(0)

        for x in range(1,amount+1):
            mincoins  = amount+1
            for c in coins:
                y = x - c
                if y < 0:
                    continue
                dy = dp[y]
                if dy is None:
                    continue
                mincoins = min(mincoins,dy)

            if mincoins != amount+1:
                dp.append(mincoins+1)
            else:
                dp.append(None)
        
        if dp[-1] is None:
            return -1
        else:
            return dp[-1]

        