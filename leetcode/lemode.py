class Solution(object):
    def lemonadeChange(self, bills):
        """
        :type bills: List[int]
        :rtype: bool
        """
        h={5:0,10:0,20:0}
        for i in range(0,len(bills)):
            if bills[i]==5:
                h[5]+=1
            elif bills[i]==10:
                if h[5]==0:
                    return False
                else:
                    h[5]-=1
                    h[10]+=1
            else:
                if  h[5]==0:
                    print(i)
                    return False
                elif h[10]==0:
                    if h[5]<3:
                      return False
                    else:
                        h[5]-=3
                else:
                    h[10]-=1
                    h[5]-=1
                
        return True

s=Solution()
print(s.lemonadeChange([5,5,10,20,5,5,5,5,5,5,5,5,5,10,5,5,20,5,20,5]))