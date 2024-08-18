class Solution:
	def removeCoveredIntervals(self, intervals):

		intervals=sorted(intervals)

		i=0
		while i<len(intervals)-1:

				a,b = intervals[i]
				p,q = intervals[i+1]

				if a <= p and q <= b:
					intervals.remove(intervals[i+1])
					i=i-1

				elif p <= a and b <= q:
					intervals.remove(intervals[i])
					i=i-1

				i=i+1
		return len(intervals)

s=Solution()
s.removeCoveredIntervals(intervals = [[1,4],[3,6],[2,8]])