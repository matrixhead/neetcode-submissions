class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        l = len(nums)
        res = 0
        for i in range(l):
            res = res ^ i+1
            res = res ^ nums[i]

        return res

        