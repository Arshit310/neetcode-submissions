class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        l1 = l2 = 0
        if sorted(s) == sorted(t):
            return True
        else:
            return False
                
        