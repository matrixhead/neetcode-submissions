class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums) -1

        result = float('inf')
        while l <= r:
            if nums [l] <= nums [r]:
                result = min(nums[l],result)
                break
            
            m = (l+r) // 2
            result = min(nums[m],result)
            if nums[l] <= nums[m]:
                l = m+1
            else:
                r = m-1
        
        return int(result)


        