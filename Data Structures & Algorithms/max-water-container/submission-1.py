class Solution:
    def maxArea(self, heights: List[int]) -> int:
        h = heights
        l = 0
        r = len(h) - 1
        max_area = 0
        while l < r:
            now_area = (r-l)*min(h[l], h[r])
            max_area = max(max_area, now_area)
            if h[l] < h[r] :
                l+=1
            else:
                r-=1
        return max_area