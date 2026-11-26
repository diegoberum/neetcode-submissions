class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights) - 1
        
        width, height = 0, 0
        maxVol = 0

        while l < r:
            height = min(heights[r], heights[l]) #1
            width = r - l #1
            area = height * width # 1
                  
            maxVol = max(maxVol, area) # 1

            if heights[r] <= heights[l]:
                r -=1
            elif heights[l] <= heights[r]:
                l += 1

        return maxVol # 



        