class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        for i,n in enumerate(nums):
            if i != 0 and n == nums[i-1]:
                continue
            l = i + 1
            r = len(nums)-1
            while l<r:
                sum = n + nums[l] + nums[r]
                if sum == 0:
                    res.append([n,nums[l],nums[r]])
                    l+=1
                elif sum < 0:
                    l+=1
                elif sum > 0:
                    r-=1
                while (l != i+1) and l<r and nums[l] == nums [l-1] :
                    l += 1
        return res


        