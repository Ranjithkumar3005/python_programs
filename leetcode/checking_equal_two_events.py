class Solution(object):
    def haveConflict(self, event1, event2):
        """
        :type event1: List[str]
        :type event2: List[str]
        :rtype: bool
        """
        return not (event1[0] > event2[1] or event1[1] < event2[0])
        
s=Solution()
print(s.haveConflict(event1 = ["01:00","02:00"], event2 = ["01:20","03:00"]))