class Solution(object):
    def corpFlightBookings(self, bookings, n):
        """
        :type bookings: List[List[int]]
        :type n: int
        :rtype: List[int]
        """
        answer = [0] * (n + 1)
        
        for first, last, seats in bookings:
            answer[first - 1] += seats
            print(answer)
            if last < n:
                answer[last] -= seats
       
        for i in range(1, n):
            answer[i] += answer[i - 1]
        
       
        return answer[:-1]
        

s=Solution()
s.corpFlightBookings(bookings = [[1,2,10],[2,3,20],[2,5,25]], n = 5)