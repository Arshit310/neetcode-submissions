class Solution:
    def myPow(self, x: float, n: int) -> float:
        t = x
        if n == 0:
            return 1.00000
        if n<0:
            for i in range(n, 0):
                x=x/t
            x=x/t
        for i in range(1, n):
            x=x*t
        return x