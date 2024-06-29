class Solution(object):
    def countMatches(self, items, ruleKey, ruleValue):
        """
        :type items: List[List[str]]
        :type ruleKey: str
        :type ruleValue: str
        :rtype: int
        """
        
        count=0
        for i in range(0,len(items)):
            if ruleKey=="type":
                if items[i][0]==ruleValue:
                    count+=1
            elif ruleKey=="color":
                if items[i][1]==ruleValue:
                    count+=1
            elif ruleKey=="name":
                if items[i][2]==ruleValue:
                    count+=1
        return count
        
        
s=Solution()
print(s.countMatches(items = [["phone","blue","pixel"],["computer","silver","phone"],["phone","gold","iphone"]], ruleKey = "type", ruleValue = "phone"))