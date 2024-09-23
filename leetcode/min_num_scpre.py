from heapq import heapify, heappop, heapreplace


class Solution:
    def minNumberOfSeconds(self, mountainHeight, workerTimes):
        heap = [(time, time, 1) for time in workerTimes]
        heapify(heap)

        while mountainHeight > 1:
            totalTime, originalTime, multiplier = heap[0]
            newMultiplier = multiplier + 1
            newTotalTime = originalTime * ((newMultiplier * (newMultiplier + 1)) // 2)
            heapreplace(heap, (newTotalTime, originalTime, newMultiplier))
            mountainHeight -= 1
            print(heap)
        return heappop(heap)[0]


s = Solution()
s.minNumberOfSeconds(mountainHeight=5, workerTimes=[1, 5])
