class Solution:
    def climbStairs(self, n: int) -> int:
        sqrt5 =  5**0.5
        phi = (1+sqrt5)/2
        return round((phi**(n+1)/sqrt5))

        