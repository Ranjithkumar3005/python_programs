# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def rangeSumBST(self, root, low, high):
        """
        :type root: TreeNode
        :type low: int
        :type high: int
        :rtype: int
        """
        sum=0
        for i in root:
            if i>=low and i<=high:
                sum+=i
        
        print(sum)
        
s=Solution()
s.rangeSumBST( root = [10,5,15,3,7,18], low = 7, high = 15)