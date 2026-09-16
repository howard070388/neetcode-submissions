class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans = []
        nums.sort()  # 原地排序，省記憶體
        
        for i in range(len(nums)):
            # 1. 基準點去重：如果這個數字跟前一個一樣，跳過避免重複三元組
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            
            # 2. 物理隔離：L 從 i + 1 出發，天生不可能跟 i 撞車
            L = i + 1
            R = len(nums) - 1
            
            while L < R:
                total = nums[i] + nums[L] + nums[R]
                
                if total > 0:
                    R -= 1
                elif total < 0:
                    L += 1
                else:
                    ans.append([nums[i], nums[L], nums[R]])
                    L += 1
                    R -= 1
                    
                    # 3. 雙指針去重：跳過相同的數值，避免收集到重複答案
                    while L < R and nums[L] == nums[L - 1]:
                        L += 1
                    while L < R and nums[R] == nums[R + 1]:
                        R -= 1
                        
        return ans