class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        save = set(nums)
        max_len = 0
        for x in save:
            if (x-1) in save:
                continue
            if (x-1) not in save:
                long = 1
                while (x + long) in save:
                    long += 1
            max_len = max(max_len, long)
        return max_len
