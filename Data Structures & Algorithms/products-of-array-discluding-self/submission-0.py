class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = []
        for i in range(len(nums)):
            if i == 0:
                res.append(1)
                continue
            prefix = res[i-1]*nums[i-1]
            res.append(prefix)

        postfix = 1
        for j in range(len(nums)-1,-1,-1):
            if j == (len(nums)-1):
                continue
            postfix = postfix * nums[j+1]
            res[j] = res[j] * postfix
        return res       