class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        dd=[]
        h={}
        for i in range(0,len(candidates)):
            dum=candidates[i]
            d=[dum]
            num=dum
            while num<target:
                print(num)
                if  target-num in candidates:
                   tem=d[::]
                   tem.append(target-num)
                   mm=str(sorted(tem))
                   if mm not in h:
                       h[mm]=0
                       dd.append(sorted(tem))
                num=num+dum
                d.append(candidates[i])
        if target in candidates:
            dd.append([target])  
        print(dd)
        

s=Solution()
s.combinationSum(candidates = [7,3,2], target = 18)