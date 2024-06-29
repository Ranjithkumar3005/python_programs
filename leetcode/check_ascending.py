class Solution(object):
    def areNumbersAscending(self, s):
        """
        :type s: str
        :rtype: bool
        """
        d=s.split(" ")
        dum=[]
        for i in d:
            if i.isdigit():
                dum.append(int(i))
        for i in range(0,len(dum)-1):
            if dum[i]<dum[i+1]:
                continue
            else:
                return False
        return True
        
        
s=Solution()
print(s.areNumbersAscending(s = "1 box has 3 blue 4 red 6 green and 12 yellow marbles"))