class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if not matrix or not matrix[0]:
            return []

        d = []
        m1, m2 = len(matrix[0]), len(matrix)  # Define the boundaries
        top, bottom, left, right = 0, m2 - 1, 0, m1 - 1  # Initialize boundaries

        while top <= bottom and left <= right:
            # Traverse from left to right along the top row
            for i in range(left, right + 1):
                d.append(matrix[top][i])
            top += 1

            # Traverse from top to bottom along the right column
            for i in range(top, bottom + 1):
                d.append(matrix[i][right])
            right -= 1
 
            # Traverse from right to left along the bottom row
            if top <= bottom:
                for i in range(right, left - 1, -1):
                    d.append(matrix[bottom][i])
                bottom -= 1

            # Traverse from bottom to top along the left column
            if left <= right:
                for i in range(bottom, top - 1, -1):
                    d.append(matrix[i][left])
                left += 1

        return d

s = Solution()
print(s.spiralOrder(matrix=[[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]))  # Expected output: [1, 2, 3, 4, 8, 12, 11, 10, 9, 5, 6, 7]
