class Solution(object):
    def twoEditWords(self, queries, dictionary):
        """
        :type queries: List[str]
        :type dictionary: List[str]
        :rtype: List[str]
        """
        result = []
        
        def is_two_edits_or_less(word1, word2):
            if len(word1) != len(word2):
                return False
            
            diff_count = 0
            for i in range(len(word1)):
                if word1[i] != word2[i]:
                    diff_count += 1
                if diff_count > 2:
                    return False
            return True
        
        for query in queries:
            for word in dictionary:
                if is_two_edits_or_less(query, word):
                    result.append(query)
                    break 
        return result

# Example usage:
s = Solution()
print(s.twoEditWords(queries=["word", "note", "ants", "wood"], dictionary=["wood", "joke", "moat"]))
