class Solution():
    def winnerOfGame(self, colors):
        """
        :type colors: str
        :rtype: bool
        """
        alice="false"
        c=colors
        n=len(colors)
        
        for i in range(1,n-1):
            if colors[i-1]==colors[i] and colors[i]==colors[i+1] and colors[i]=='A':
                print(colors[i])
                index = i
                new_char = ''

                string_list = list(colors)
                string_list[index] = new_char
                new_string = "".join(string_list)
                alice="true"
                break
        for i in range(1,n-1):
            if colors[i-1]==colors[i] and colors[i]==colors[i+1] and colors[i]=='B':
                print(colors[i])
                index = i
                new_char = ''

                string_list = list(colors)
                string_list[index] = new_char
                new_string = "".join(string_list)
                alice="false"
                break  
        return alice

s=Solution()
print(s.winnerOfGame("AA"))