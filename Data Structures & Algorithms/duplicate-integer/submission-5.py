class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        save = set()
        for num in nums:
            if num in save:
                return True
            save.add(num)
        return False