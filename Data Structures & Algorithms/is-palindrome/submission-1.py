class Solution:
    def isPalindrome(self, s: str) -> bool:
        alpha = ""
        for ch in s:
            if ch.isalnum():
                alpha += alpha.join(ch)
        rev = ""
        for c in alpha[::-1]:
            rev+=rev.join(c)
        if alpha.upper()==rev.upper():
            return True
        else:
            return False
