class Solution:
    def findMin(self, nums: List[int]) -> int:
        # max index & min index = right & left        
        # mid_index判斷 if right < mid ：保留右邊（捨棄左邊界）
        # mid_index判斷 else： 最小值在mid or 左邊 丟了右邊但留mid
        left = 0
        right = len(nums) - 1
        
        while left < right:
            mid = (right+left) // 2 
            if nums[right] < nums[mid] :
                left = mid + 1
            else:
                right = mid
        return nums[left]