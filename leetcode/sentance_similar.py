class Solution(object):
    def areSentencesSimilar(self, sentence1, sentence2):
        """
        :type sentence1: str
        :type sentence2: str
        :rtype: bool
        """
        str1 = sentence1.split(" ")
        str2 = sentence2.split(" ")
        
        if len(str1) > len(str2):
            str1, str2 = str2, str1
        
        i = 0
        j = len(str1) - 1
        k = len(str2) - 1
        
        while i <= j and str1[i] == str2[i]:
            i += 1
        
        while j >= i and str1[j] == str2[k]:
            j -= 1
            k -= 1
        
        return i > j

# Example usage:
s = Solution()
print(s.areSentencesSimilar(sentence1 = "My name is Haley", sentence2 = "My Haley"))  # Output: True
print(s.areSentencesSimilar(sentence1 = "My name is Haley", sentence2 = "My name"))  # Output: False
