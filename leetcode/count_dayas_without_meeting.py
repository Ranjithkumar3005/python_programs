class Solution(object):
    def countDays(self, days, meetings):
        """
        :type days: int
        :type meetings: List[List[int]]
        :rtype: int
        """
        # Create a difference array to track the intervals
        diff = [0] * (days + 2)  # days + 2 to handle the boundary at days + 1
        
        # Apply the difference array technique
        for start, end in meetings:
            diff[start] += 1
            if end + 1 <= days:
                diff[end + 1] -= 1
                print(diff)
        
        # Calculate the number of free days
        ongoing_meetings = 0
        free_days = 0
        for i in range(1, days + 1):
            ongoing_meetings += diff[i]
            if ongoing_meetings == 0:
                free_days += 1
        
        return free_days


s=Solution()
s.countDays(days = 10, meetings = [[5,7],[1,3],[9,10]])