class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        save = {}
        for i , num in enumerate(nums):
            need = target - num
            if need not in save:
                save[num] = i
            else:
                return [save[need],i]