class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        arr = prices
        l = 0
        r = 1
        max_sum = 0
        while r < len(arr):
            if arr[l] < arr[r]:
                max_sum = max(max_sum, arr[r] - arr[l])
            else:
                l = r
            r+=1

        return max_sum
        