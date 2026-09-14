class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        save={}
        for i , num in enumerate(numbers):
            need = target - num
            if need in save:
                return [save[need]+1,i+1]
            save[num] = i