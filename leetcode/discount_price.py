class Solution(object):
    def discountPrices(self, sentence, discount):
        """
        :type sentence: str
        :type discount: int
        :rtype: str
        """
        words = sentence.split(" ")
        result = []

        for word in words:
            if word.startswith("$") and word[1:].isdigit():
                price = float(word[1:])  
                discounted_price = price - (price * discount / 100) 
                result.append("${:.2f}".format(discounted_price)) 
            else:
                result.append(word) 

        return " ".join(result) 

s = Solution()
print(s.discountPrices(sentence="1 2 $3 4 $5 $6 7 8$ $9 $10$", discount=100))
