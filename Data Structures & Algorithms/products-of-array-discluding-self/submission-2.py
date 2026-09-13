class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = [1]
        suffix = [1]
        save=[]
        total = 1
        for num in nums:
            total *= num
            prefix.append(total)
        total = 1

        for i in range(len(nums)-1, -1, -1):
            total *= nums[i]
            suffix.append(total)
        suffix.reverse()

        for i in range(len(nums)):
            final = prefix[i]*suffix[i+1]
            save.append(final)

        return save