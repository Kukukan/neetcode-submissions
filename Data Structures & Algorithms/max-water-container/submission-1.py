class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0
        right = len(heights) - 1
        max_water = 0
        while left < right:
            width = right-left
            current_height = min(heights[left], heights[right])

            current_water = width*current_height

            # assign result
            max_water = max(current_water, max_water)
            
            # move two pointers
            if heights[left] < heights[right]:
                left += 1
            else:
                right -=1
        return max_water


        