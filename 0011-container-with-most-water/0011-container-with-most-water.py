class Solution:
    def maxArea(self, height: List[int]) -> int:
        start = 0
        end = len(height)-1
        x_width = end
        area = 0

        while start<end:
            area = max(area, x_width*min(height[start],height[end])) 
            if height[start]<height[end]:
                start+=1
                x_width-=1
            else:
                end-=1
                x_width-=1
        return area