class Solution(object):
    def arrayRankTransform(self, arr):
        """
        :type arr: List[int]
        :rtype: List[int]
        """
        elements_ascending = sorted(set(arr))
        # dictionary
        # key   : number
        # value : rank
        num_rank_dict = dict()
        for index, num in enumerate(elements_ascending):
            # rank = index + 1
            num_rank_dict[num] = (index+1)
        # give each number with its corresponding rank
    
        result = [ num_rank_dict[num] for num in arr ]
        print(result)
        
s=Solution()
s.arrayRankTransform( arr = [37,12,28,9,100,56,80,5,12])