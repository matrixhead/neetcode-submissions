class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        result = []

        def dfs(i:int,comb:List[int],total:int):
            #base case
            if total == target:
                result.append(comb.copy())
                return
            #constraint
            if (i >=len(nums)) or total > target:
                return
            #we have two choices
            comb.append(nums[i])
            dfs(i=i,comb=comb,total=total+nums[i])
            #now backtrack
            comb.pop()
            dfs(i=i+1,comb=comb,total=total)

        dfs(i=0,comb=[],total=0)
        return result





        