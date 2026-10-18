class TimeMap:

    def __init__(self):
        self.store = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.store:
            self.store[key] = []
        self.store[key].append((value, timestamp))

    def get(self, key: str, timestamp: int) -> str:
        ans = ""
        if key not in self.store:
            return ans
        left = 0
        right = len(self.store[key]) - 1
        while left <= right:
            mid = (left + right) // 2
            if self.store[key][mid][1] <= timestamp:
                left = mid + 1
                ans = self.store[key][mid][0]
            else:
                right = mid -1
        return ans