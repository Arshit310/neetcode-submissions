class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        s = {}
        for i, num in enumerate(numbers):
            if target - num in s:
                return [s[target-num], i+1]
            s[num] = i+1

        