class Solution(object):
    def maxDistToClosest(self, seats):
        """
        :type seats: List[int]
        :rtype: int
        """
        h=0
        c=0
        max=0
        check=False
        d=0
        for i in seats:
            if i==0:
                c+=1
            if i==1 and not check:
                check=True
                if max<c:
                    max=c
                c=0
            elif i==1 and check:
                c+=1
                check=True
                if max<c//2:
                    max=c//2
                c=0
        if c>max:
            max=c
        print(max)

s=Solution()
s.maxDistToClosest(seats =[1,1,0,0,0,1,0])