class Solution:
    def maxArea(self, heights: List[int]) -> int:

        res = 0

        left = 0
        right = len(heights)-1

        while left < right:

            if heights[left] < heights[right]:
                max_h = heights[left]
                width = (right - left) * max_h
                res = max(res, width)
                left += 1
            else:
                max_h = heights[right]
                width = (right - left) * max_h
                
                res = max(res, width)
                
                right -= 1
        return res

            
        