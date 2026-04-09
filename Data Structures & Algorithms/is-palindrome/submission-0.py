import re
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()

        pattern = r"[^a-z0-9]"

        result = re.sub(pattern,'',s)

        return result == result[::-1]
        