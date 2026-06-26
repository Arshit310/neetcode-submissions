class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        n = len(matrix)
        m = len(matrix[0])

        l = 0
        r = n*m -1
        while l <= r:
            mid = l+(r-l)//2
            row = mid//m
            col = mid%m

            mid_val = matrix[row][col]

            if mid_val == target:
                return True
            elif mid_val < target:
                l = mid +1
            else:
                r = mid - 1
        return False
        