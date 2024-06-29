class Solution(object):
    def slowestKey(self, releaseTimes, keysPressed):
        """
        :type releaseTimes: List[int]
        :type keysPressed: str
        :rtype: str
        """
        dur=releaseTimes[0]
        m=keysPressed[0]
        for i in range(1,len(releaseTimes)):
            dum=releaseTimes[i]-releaseTimes[i-1]
            if dur<=dum:
                if dur==dum:
                    if m<keysPressed[i]:
                        m=keysPressed[i]
                else:
                    dur=dum
                    m=keysPressed[i]
        print(m)
        
        
        
        
        
s=Solution()
s.slowestKey(releaseTimes = [9,29,49,50], keysPressed = "cbcd")