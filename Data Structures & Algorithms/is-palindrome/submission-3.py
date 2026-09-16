class Solution:
    def isPalindrome(self, s: str) -> bool:
        clean_result = [result.lower() for result in s if result.isalnum()]
        clean_result2 = clean_result[: : -1]
        if clean_result == clean_result2:
            return True
        return False
