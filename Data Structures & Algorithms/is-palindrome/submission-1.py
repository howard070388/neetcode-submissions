class Solution:
    def isPalindrome(self, s: str) -> bool:
        base = []
        ud_base = []
        for i in range(len(s)):
            num = s[i]
            if num.isalnum():
                nnum=num.lower()
                base.append(nnum)
        for j in range(len(s)-1,-1,-1):
            num2 = s[j]
            if num2.isalnum():
                nnum2=num2.lower()
                ud_base.append(nnum2)
        return base == ud_base

