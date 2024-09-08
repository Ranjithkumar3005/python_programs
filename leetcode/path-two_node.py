from collections import deque
class Solution(object):
    def path_two_nodes(self, nums,s,e):
        queue=deque([s])
        visited=set()
        visited.add(s)
        while queue:
            val=queue.popleft()
            if val==e:
                return True
            for i in nums[val]:
                if i not in visited:
                    queue.append(i)
                    visited.add(i)
        return False
                    
        

s=Solution()
print(s.path_two_nodes(nums= {0: [1, 2],1: [0, 3, 4],2: [0, 4],3: [1],4: [1, 2]},s=0,e=3))