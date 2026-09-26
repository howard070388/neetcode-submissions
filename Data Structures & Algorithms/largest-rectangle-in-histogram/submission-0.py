class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        max_area = 0

        for i in range(len(heights)):
            new_start = i
            while stack and heights[i] < stack[-1][1]:
                pop_start, height = stack.pop()
                width = i - pop_start
                area = height * width
                max_area = max(max_area, area)
                new_start = pop_start
            stack.append((new_start, heights[i]))

        while stack:
            start, height = stack.pop()

            width = len(heights) - start
            area = height * width
            max_area = max(max_area, area)

        return max_area