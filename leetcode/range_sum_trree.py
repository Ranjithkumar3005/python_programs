class Solution:
    def rangeSumBST(self, root,low, high):
        def dfs(node):
            if not node:
                return 0
            
            current_val = 0
            if low <= node.val <= high:
                current_val = node.val
            
            left_sum = dfs(node.left)
            right_sum = dfs(node.right)
            
            return current_val + left_sum + right_sum
        
        return dfs(root)
s=Solution()
print(s.rangeSumBST([7,4,3,8,9,12,0,2],7,12))