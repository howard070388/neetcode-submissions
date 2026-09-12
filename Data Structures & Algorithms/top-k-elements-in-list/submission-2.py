class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        save = {}
        for num in nums:
            if num in save:
                save[num] += 1
            else:
                save[num] = 1
        return sorted(save, key = save.get, reverse = True )[:k]