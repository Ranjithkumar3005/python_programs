from sortedcontainers import SortedList

class Solution(object):
    def containsNearbyAlmostDuplicate(self, nums, indexDiff, valueDiff):
        """
        :type nums: List[int]
        :type indexDiff: int
        :type valueDiff: int
        :rtype: bool
        """
        if indexDiff <= 0 or valueDiff < 0:
            return False

        window = SortedList()
        for i in range(len(nums)):
            # Remove the element that is too far away in terms of index
            if i > indexDiff:
                window.remove(nums[i - indexDiff - 1])

            # Find the position to insert the current number
            pos = window.bisect_left(nums[i] - valueDiff)

            # Check if there is any number in the window that satisfies the valueDiff condition
            if pos < len(window) and abs(window[pos] - nums[i]) <= valueDiff:
                return True

            # Add the current number to the window
            window.add(nums[i])

        return False

s = Solution()
print(s.containsNearbyAlmostDuplicate(nums=[1421, 2433, 3054, 9952, 6470, 8502, -8802, -5276, 6559, -9555, -4765, 6399, 6543, 2027, 1723, -3032, -3319, -7726, -1425, -7431, -7492, 4803, 7952, -6603, -784, -8011, 6161, -6955, 5800, 5834, -6310, 1097, 2327, -4007, 8664, -9619, 5922, 518, 9740, 9976, 4257, -7803, 6023, 4189, -5167, -4699, 2441, 5941, 3663, 625, 5402, -3447, 8888, 9040, -4811, -7547, 6822, 1415, 9372, -9262, 4584, 4149, -276, -4019, 198, 608, -4466, 5383, 7871, 3149, -8358, 9270, 3565, -882, -9494, -6475, 9833, -7744, -598, 5299, 5976, 7361, -9444, 3771, -5718, 9051, 3469, -402], indexDiff=1, valueDiff=0))
