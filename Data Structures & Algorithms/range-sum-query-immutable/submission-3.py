class NumArray:

    def __init__(self, nums: List[int]):
        prefix=[0]
        total = 0
        for num in nums:
            total += num
            prefix.append(total)
        self.prefix = prefix
    def sumRange(self, left: int, right: int) -> int:
        profix_right = self.prefix[right+1]
        profix_left = self.prefix[left]
        return profix_right - profix_left
# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)