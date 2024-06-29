class Solution(object):
    def minMovesToSeat(self, seats, students):
        """
        :type seats: List[int]
        :type students: List[int]
        :rtype: int
        """
        seats=sorted(seats)
        students=sorted(students)
        tot=0
        for i in range(0,len(seats)):
            tot+=abs(seats[i]-students[i])
        print(tot)
        
s=Solution()
s.minMovesToSeat(seats = [3,1,5], students = [2,7,4])