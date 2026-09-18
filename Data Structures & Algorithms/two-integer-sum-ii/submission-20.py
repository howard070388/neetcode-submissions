class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        nums = numbers
        L = 0
        R = len(nums) - 1
        while L < R:
            total = nums[L] + nums[R]
            if total > target :
                R -= 1
            elif total < target :
                L += 1
            else:
                return [L+1, R+1]