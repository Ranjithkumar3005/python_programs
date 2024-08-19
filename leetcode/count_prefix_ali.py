class Solution(object):
    def countPrefixAlignments(self, flips):
        """
        :type flips: List[int]
        :rtype: int
        """
        max_flipped_index = 0
        prefix_count = 0
        
        for step, flip in enumerate(flips):
            max_flipped_index = max(max_flipped_index, flip)
            print(max_flipped_index)
            if max_flipped_index == step + 1:
                prefix_count += 1
        
        return prefix_count

# Example usage
s = Solution()
print(s.countPrefixAlignments(flips = [3,2,4,1,5]))  # Example output
