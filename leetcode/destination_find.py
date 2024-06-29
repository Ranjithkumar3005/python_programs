class Solution(object):
    def destCity(self, paths):
        """
        :type paths: List[List[str]]
        :rtype: str
        """
        d = {}
        for elem in paths:
           if elem[1] in d:
              d[elem[1]].append(elem[0])
           else:
              d[elem[1]] = [elem[0]]
        count=0
        count1=0
        dummy=self.string(d[list(d)[0]])   
        start=""   
        
        for i in range(0,len(paths)):
            count+=1
            if dummy==list(d)[i]:
                count1+=1
                dummy=self.string(d[list(d)[count1]])
                start=dummy
            if count==len(paths):
                start=dummy
        i=0
        while i<len(paths):
            if self.string(d[list(d)[i]])==start:
                start=list(d)[i]     
                i=0 
                continue
            i+=1
        print(start)
    def string(self,data):
        dummy=""
        for i in range(0,1):
            dummy=data[i]
        return dummy
    
s=Solution()
s.destCity( [["A","Z"]])