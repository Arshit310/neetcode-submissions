class Solution:
    def isPalindrome(self, s: str) -> bool:
        strs = "".join(i for i in s.lower() if i.isalpha() or i.isdigit())
        l = 0
        r = len(strs)-1
        while l<r:
            if strs[l] != strs[r]:
                return False
            l+=1
            r-=1
        return True
        