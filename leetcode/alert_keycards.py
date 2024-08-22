class Solution(object):
    def alertNames(self, keyName, keyTime):
        """
        :type keyName: List[str]
        :type keyTime: List[str]
        :rtype: List[str]
        """
        from collections import defaultdict
        h = defaultdict(list)
        
        for i in range(len(keyName)):
            hours, minutes = map(int, keyTime[i].split(':'))
            total_minutes = hours * 60 + minutes
            h[keyName[i]].append(total_minutes)
        print(h)
        dum = []
        for name, times in h.items():
            times.sort()  
            for j in range(len(times) - 2):
                if times[j + 2] - times[j] <= 60:
                    dum.append(name)
                    break
        
        return sorted(dum)

s = Solution()
print(s.alertNames(keyName=["daniel","daniel","daniel","luis","luis","luis","luis"], 
                   keyTime=["10:00","10:40","11:00","09:00","11:00","13:00","15:00"]))
