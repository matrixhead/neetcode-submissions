class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = 0
        r = len(heights)-1
        la = 0
        while l<r:
            lh = heights[l]
            rh = heights[r]
            width = r-l
            height = min(lh,rh)
            a = width * height
            if a > la:
                la = a
            if height == lh:
                l = l+1
            else:
                r = r-1
        return la

