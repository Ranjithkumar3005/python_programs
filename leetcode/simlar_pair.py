class Solution(object):
    def similarPairs(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        # Create a list of sets of unique characters for each word
        unique_char_sets = [set(word) for word in words]
        
        # Initialize the counter for similar pairs
        c = 0
        
        # Compare each pair of unique character sets
        for i in range(len(unique_char_sets)):
            for j in range(i + 1, len(unique_char_sets)):
                if unique_char_sets[i] == unique_char_sets[j]:
                    c += 1
        
        return c



s=Solution()
print(s.similarPairs(words = ["aba","aabb","abcd","bac","aabc"]))