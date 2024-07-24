from collections import Counter

class Solution(object):
    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        word_length = len(words[0])
        total_length = word_length * len(words)
        word_count = Counter(words)
        print(word_count)
        result = []
        
        for i in range(len(s) - total_length + 1):
            substring = s[i:i + total_length]
            substring_count = Counter([substring[j:j + word_length] for j in range(0, total_length, word_length)])
            if substring_count == word_count:
                result.append(i)
        return result

solution = Solution()
s = "foobarfoobar"
words = ["foo", "bar"]
print(solution.findSubstring(s, words))  # Output: [0, 3, 6]
