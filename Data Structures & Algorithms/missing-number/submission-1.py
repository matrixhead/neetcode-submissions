class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        l = len(nums)
        res = 0
        for i in range(l):
            print(i+1)
            print(nums[i])
            res = res ^ i+1
            res = res ^ nums[i]

        return res

        