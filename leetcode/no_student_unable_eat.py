class Solution(object):
    def countStudents(self, students, sandwiches):
        """
        :type students: List[int]
        :type sandwiches: List[int]
        :rtype: int
        """
        dum=students
        dum1=sandwiches
        i=0
        while True:
            if dum[0]==dum1[0]:
                dum.remove(dum[0])
                dum1.remove(dum1[0])
                i=0
            else:
                i+=1
                d=dum[0]
                dum.remove(d)
                dum.append(d)
                print(dum)
            if i==len(dum):
                break
        print(dum)
                
        
        
s=Solution()
s.countStudents(students = [1,1,1,0,0,1], sandwiches = [1,0,0,0,1,1])