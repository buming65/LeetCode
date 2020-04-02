class Solution:
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not matrix:
            return False
        def search(left, up, right, down):
            if left > right or up > down:
                return False
            if target < matrix[up][left] or target > matrix[down][right]:
                return False
            
            mid = left + (right - left)//2
            
            # Locate
            row = up
            while row <= down and matrix[row][mid] <= target:
                if matrix[row][mid] == target:
                    return True
                row += 1
            return search(left, row, mid - 1, down) or search(mid + 1, up, right, row - 1)
        
        return search(0, 0, len(matrix[0]) - 1, len(matrix) - 1)


class Solution:
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not matrix:
            return False
        row = len(matrix)
        col = len(matrix[0])
        
        r = row - 1
        c = 0
        
        while r >= 0 and c < col:
            if matrix[r][c] > target:
                r -= 1
            elif matrix[r][c] < target:
                c += 1
            else:
                return True
        return False