class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = [1] * len(nums)
        res = 1
        for i in range(len(nums)):
            n = nums[i]
            maximum = 0
            for j in range(i):
                if nums[j]< n:
                    maximum = max(maximum,dp[j])
            dp[i] = maximum + 1
            res = max(dp[i],res)

        return res

            

        