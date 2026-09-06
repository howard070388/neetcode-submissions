class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        count_s={}
        count_t={}
        for catch_s in s:
            if catch_s in count_s:
                count_s[catch_s] += 1
            else :
                count_s[catch_s] = 1
        for catch_t in t:
            if catch_t in count_t:
                count_t[catch_t] += 1
            else :
                count_t[catch_t] = 1
        return count_s == count_t