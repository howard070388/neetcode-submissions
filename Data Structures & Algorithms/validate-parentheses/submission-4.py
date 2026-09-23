class Solution:
    def isValid(self, s: str) -> bool:
        ans = []
        for word in s:
            if word == '(' or word == '[' or word == '{':
                ans.append(word)
            elif ans and (word == ')' and ans[-1] == '('
            or word == ']' and ans[-1] == '['
            or word == '}' and ans[-1] == '{'):
                ans.pop()
            else:
                return False
        return ans == []
