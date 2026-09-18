class Solution:
    def trap(self, height: List[int]) -> int:
        h = height
        L = 0
        R = len(h) -1
        totalw = 0
        left_max = h[L]
        right_max = h[R]
        while L < R:
            if left_max >= right_max:
                R -=1
                if h[R] >= right_max:
                    right_max = h[R]
                else:
                    water = right_max - h[R]
                    totalw += water
            else:
                L+=1
                if h[L] >= left_max:
                    left_max = h[L]
                else:
                    water = left_max - h[L]
                    totalw += water
        return totalw