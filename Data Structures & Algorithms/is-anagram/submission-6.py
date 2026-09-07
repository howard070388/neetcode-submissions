class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        cs={}
        ct={}
        for key in s:
            if key in cs:
                cs[key] += 1
            else:
                cs[key] = 1
        for key in t:
            if key in ct:
                ct[key] += 1
            else:
                ct[key] = 1
        return cs == ct
            