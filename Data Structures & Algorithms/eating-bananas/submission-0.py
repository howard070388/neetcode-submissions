class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        right = max(piles)
        left = 1
        while left < right:
            mid_k = (right+left) // 2
            total_h = 0
            for pile in piles:
                spend_h = ( pile + (mid_k-1) ) // mid_k 
                total_h += spend_h
            if total_h <= h:
                right = mid_k
            else:
                left = mid_k + 1
        return left