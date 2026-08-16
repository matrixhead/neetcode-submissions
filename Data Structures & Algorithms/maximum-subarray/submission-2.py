class Solution:
    def maxSubArray(self, nums: List[int]) -> int:

        maximum = float("-inf")
        ret = maximum 

        for num in nums:
            maximum = max(maximum+num,num)
            ret = max(ret,maximum)
            
        return int(ret)

            
        