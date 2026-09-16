class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        Ans = []
        nums.sort()
        
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                continue
                
            R = len(nums) -1
            L = i+1
            
            while L < R:
                total = nums[i] + nums[L] + nums[R]
                
                if total > 0:
                    R-=1
                elif total < 0:
                    L+=1
                else:
                    Ans.append([nums[i],nums[L], nums[R]])
                    R-=1
                    L+=1
                    while L < R and nums[L] == nums[L-1]:
                        L += 1
                    while L < R and nums[R] == nums[R+1]:
                        R -= 1
        return Ans