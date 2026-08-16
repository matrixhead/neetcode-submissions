class Solution:
    def canJump(self, nums: List[int]) -> bool:
        
        i = len(nums)-1
            
        for j in range(i-1,-1,-1):
            distance = i-j
            if nums[j] >= distance:
                i = j
        return i == 0