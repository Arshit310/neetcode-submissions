class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        a = "".join(str(i) for i in digits)
        return (list(str(int(a)+1)))
        