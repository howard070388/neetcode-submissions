class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        n = numbers.copy()
        r = len(n) - 1
        l = 0
        while l < r:
            if n[l] + n[r] > target:
                r -= 1
            elif n[l] + n[r] < target:
                l += 1
            else:
                return [l+1, r+1]