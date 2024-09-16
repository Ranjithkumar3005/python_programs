class Solution:
    def combination(self,nums,target):
        res=[]
        
        def dfs(i,curr,tot):
            if target==tot:
                res.append(curr[:])
                return
            if i>=len(nums) or tot>target:
                return 
            
            curr.append(nums[i])
            dfs(i,curr,tot+nums[i])
            curr.pop()
            dfs(i+1,curr,tot)
        dfs(0,[],0)
        print(res)
    
s=Solution()
s.combination([2,3,6,7],7)