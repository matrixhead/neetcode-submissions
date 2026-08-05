class Solution:
    def rob(self, nums: List[int]) -> int:
        l = len(nums)
        if l == 1:
            return nums[0]
        a = nums[0]
        b = max(a, nums[1])
        for i in range(2,l):
            temp = a
            a = b
            b = max(b, nums[i] + temp)

        return b
        