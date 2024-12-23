from collections import deque


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def minimumOperations(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        que = deque([root])
        op = 0

        while que:
            level_size = len(que)
            values = []
            for _ in range(level_size):
                node = que.popleft()
                values.append(node.val)

                if node.left:
                    que.append(node.left)
                if node.right:
                    que.append(node.right)

            sorted_values = sorted(values)
            if values != sorted_values:
                op += self.minSwaps(values, sorted_values)

        return op

    def minSwaps(self, original, sorted_array):
        """
        Calculate the minimum swaps needed to transform the original array into the sorted array.
        :param original: Original array
        :param sorted_array: Sorted version of the array
        :return: Minimum number of swaps
        """
        index_map = {value: i for i, value in enumerate(sorted_array)}
        visited = [False] * len(original)
        swaps = 0

        for i in range(len(original)):
            if visited[i] or index_map[original[i]] == i:
                continue

            # Cycle detection
            cycle_size = 0
            j = i
            while not visited[j]:
                visited[j] = True
                j = index_map[original[j]]
                cycle_size += 1

            if cycle_size > 1:
                swaps += cycle_size - 1

        return swaps
