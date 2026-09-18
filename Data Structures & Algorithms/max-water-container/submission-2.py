class Solution:
    def maxArea(self, heights: List[int]) -> int:
        h = heights
        L = 0
        R = len(h) - 1
        max_area = 0
        while L < R:
            cur_area = (R - L)*min(h[L],h[R])
            max_area = max(max_area, cur_area)
            if h[L] <= h[R]:
                L+=1
            else:
                R-=1
        return max_area