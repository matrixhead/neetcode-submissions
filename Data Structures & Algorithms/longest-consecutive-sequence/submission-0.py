class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hset = set(nums)
        lcs = 0
        for n in nums:
            if (n-1) in hset:
                continue
            i = 1
            while (n+i) in hset:
                i = i+1
            if lcs <= i:
                lcs = i
        return lcs
