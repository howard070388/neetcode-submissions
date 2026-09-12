class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        save = {}
        for i, num in enumerate(nums):
            need = target - num
            if need in save:
                return [save[need],i]
            save[num]=i
        