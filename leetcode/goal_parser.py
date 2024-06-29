class Solution(object):
    def interpret(self, command):
        """
        :type command: str
        :rtype: str
        """
        command=command.replace("()","o").replace("(al)","al")
        print(command)
        
        
        
s=Solution()
s.interpret(command = "(al)G(al)()()G")