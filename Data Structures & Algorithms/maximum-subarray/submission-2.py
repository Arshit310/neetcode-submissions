class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        s = smax = nums[0]
        for i in nums[1:]:
            if s < 0:
                s=0
            s+=i
            smax = max(smax, s)
        return smax
            
        