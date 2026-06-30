class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        down_two = cost[0]
        down_one = cost[1]

        for i in range(2, len(cost)):
            cur = cost[i] + min(down_one, down_two)
            down_two = down_one
            down_one = cur
        return min(down_one, down_two)        