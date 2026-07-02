class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()
        
        l = r= maxcount = 0
        while r<len(s):
            if s[r] not in seen:
                seen.add(s[r])
                r+=1
                maxcount = max(maxcount, r-l)
            else:
                seen.remove(s[l])
                l+=1
        return maxcount
        