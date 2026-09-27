class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        max_area = 0
        for i in range(len(heights)):
            new_start = i
            while stack and heights[i] < stack[-1][1]:
                pop_start, height = stack.pop()
                wid = i - pop_start
                area = wid * height
                max_area = max(max_area, area)
                new_start = pop_start
            stack.append((new_start, heights[i]))
        while stack:
            start, height = stack.pop()
            wid = len(heights) - start
            area = wid * height
            max_area = max(max_area, area)

        return max_area