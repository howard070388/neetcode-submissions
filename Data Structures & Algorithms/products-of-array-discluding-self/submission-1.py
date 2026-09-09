class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ex=[1]*len(nums)
        i = 0
        total = 1
        while i < len(nums):
            ex[i] = total
            total *= nums[i]
            i += 1 

        total = 1

        i = len(nums) - 1
        while i >= 0:
            ex[i] *= total
            total *= nums[i]
            i -= 1
        
        return list(ex)