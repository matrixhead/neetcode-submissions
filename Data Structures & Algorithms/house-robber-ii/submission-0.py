class Solution:
    def rob(self, nums: List[int]) -> int:
        return max(nums[0],self.helper(nums[1:]),self.helper(nums[:-1]))

    
    def helper(self,nums:List[int]) -> int:
        a,b = 0,0
        for n in nums:
            new_rob = max(b,a+n)
            a = b
            b = new_rob
        return b

        