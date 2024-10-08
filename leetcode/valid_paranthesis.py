class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        open_list = ["[","{","("]
        close_list = ["]","}",")"]
        stack = []
        for i in s:
            if i in open_list:
               stack.append(i)
            elif i in close_list:
               pos = close_list.index(i)
               if ((len(stack) > 0) and
                  (open_list[pos] == stack[len(stack)-1])):
                   stack.pop()
               else:
                   return "Unbalanced"
        if len(stack) == 0:
            return True
        else:
            return False
    
s=Solution()
print(s.isValid("(]"))