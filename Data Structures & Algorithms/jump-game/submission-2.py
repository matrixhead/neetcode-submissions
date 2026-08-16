class Solution:
    def canJump(self, nums: List[int]) -> bool:
        
        i = len(nums)-1
            
        for j in range(i-1,-1,-1):
            distance = i-j
            if nums[j] >= distance:
                print(f"i is {i} j is {j}")
                i = j
        return i == 0