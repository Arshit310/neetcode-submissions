class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        def backtrack(r, i):
            if i == n:
                res.append(list(r))
                return
            for j in range(i, n):
                r[i], r[j] = r[j], r[i]
                backtrack(r, i+1)
                r[i], r[j] = r[j], r[i]
        res = []
        backtrack(nums, 0)
        return res
        