class Solution(object):
    def survivedRobotsHealths(self, positions, healths, directions):
        """
        :type positions: List[int]
        :type healths: List[int]
        :type directions: str
        :rtype: List[int]
        """
        h1={}
        h2={}
        for i in range(0,len(positions)):
            h1[positions[i]]=healths[i]
            h2[positions[i]]=directions[i]
        dum=sorted(h1.keys())
        st=[]
        st1=[]
        st.append(h1[dum[0]])
        st1.append(h2[dum[0]])
        print(h1," ",h2)
        for i in range(1,len(dum)):
            if st1[len(st1)-1]!=h2[dum[i]]:
                if st[len(st)-1]>h1[dum[i]]:
                   st[len(st)-1]=st[len(st)-1]-1
                elif st[len(st)-1]==h1[dum[i]]:
                    st.pop()
                    st1.pop()
                else:
                    st[len(st1)-1]=h1[dum[i]]-1
                    st1[len(st1)-1]=h2[dum[i]]
            else:
                st.append(dum[i])
                st1.append(h2[dum[i]])
        print(st)    
        
s=Solution()
s.survivedRobotsHealths( positions = [3,5,2,6], healths = [10,10,15,12], directions = "RLRL")