class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        save={}
        for num in nums:
            key = num
            if key in save:
                save[key] += 1
            else:
                save[key] = 1
        sorted_keys = sorted(save, key=save.get, reverse = True)
        return sorted_keys[:k]