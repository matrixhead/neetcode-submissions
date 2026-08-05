class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        maximum = nums[0]
        dp = nums[0]
        dp2 = nums[0]
        for i in range(1,len(nums)):
            n = nums[i]
            temp = dp
            dp = max(n, n * dp, n*dp2)
            print(f"dp is {dp}")
            dp2 = min(n, n * dp2,n*temp)
            print(f"dp2 is {dp2}")
            maximum = max(maximum,dp)


        return maximum
        