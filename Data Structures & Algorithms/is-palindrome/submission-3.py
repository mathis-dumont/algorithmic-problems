import re
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()

        pattern = r"[^a-z0-9]"

        s = re.sub(pattern,'',s)

        return s == s[::-1]