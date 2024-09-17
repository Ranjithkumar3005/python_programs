class Solution(object):
    def sortTheStudents(self, score, k):
        """
        :type score: List[List[int]]
        :type k: int
        :rtype: List[List[int]]
        """
        vals=[]
        for i in score:
            vals.append(i[k])
        vals.sort(reverse=True)
        dums=[0]*len(vals)
        for i in score:
            ind=vals.index(i[k])
            dums[ind]=i
        print(dums)
        
        

s=Solution()
s.sortTheStudents(score = [[10,6,9,1],[7,5,11,2],[4,8,3,15]], k = 2)