class Solution(object):
    def maximumPrimeDifference(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        primes=[2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89,97]
        firstprime=0
        lastprime=0
        for i in range(len(nums)):
            if nums[i] in primes:
                firstprime=i
                break
        for i in range(len(nums)-1,-1,-1):
            if nums[i] in primes:
                lastprime=i
                break
        
        print(lastprime-firstprime)

s=Solution()
s.maximumPrimeDifference(nums = [4,2,9,5,3])