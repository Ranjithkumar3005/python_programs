class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        open_list = ["[","{","("]
        close_list = ["]","}",")"]
        stack = []
        count=0
        for i in s:
            if i in open_list:
               stack.append(i)
            elif i in close_list:
               pos = close_list.index(i)
               if ((len(stack) > 0) and
                  (open_list[pos] == stack[len(stack)-1])):
                   stack.pop()
                   count+=1
               else:
                   print("sf")
        print(count*2)
    
s=Solution()
s.longestValidParentheses("()(()")