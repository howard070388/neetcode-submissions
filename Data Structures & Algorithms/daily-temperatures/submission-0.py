class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        tem = temperatures
        save = []
        ans = [0]*len(tem)
        for i in range(len(tem)):
            while save and tem[i] > tem[save[-1]]:
                pre = save.pop()
                days = i - pre
                ans[pre] = days

            save.append(i)
        return ans