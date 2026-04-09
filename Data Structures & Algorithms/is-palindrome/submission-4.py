class Solution:
    def isPalindrome(self, s: str) -> bool:


        l, r = 0, len(s)-1
        if s =="":
            return True

        while l<r:
            while l<r and not self.isalphanum(s[l]):
                l+=1
            while l<r and not self.isalphanum(s[r]):
                r-=1
            if s[r].lower()!=s[l].lower():
                return False
            l+=1
            r-=1
        return True

    def isalphanum(self,c):
        return (ord('a')<=ord(c.lower()) and ord(c.lower())<=ord('z')) or (ord('0')<=ord(c) and ord(c)<=ord('9'))