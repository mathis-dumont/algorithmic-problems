import re
class Solution:
    def isPalindrome(self, s: str) -> bool:
        # s = s.lower()

        # pattern = r"[^a-z0-9]"

        # result = re.sub(pattern,'',s)

        # return result == result[::-1]
        
        s = s.lower()

        result = ''.join(letter for letter in s if letter.isalnum())

        return result == result[::-1]