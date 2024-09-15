class Solution(object):
    def shiftingLetters(self, s, shifts):
        """
        :type s: str
        :type shifts: List[List[int]]
        :rtype: str
        """
        h={}
        for i in shifts:
            for j in range(i[0],i[1]+1):
                if j in h:
                    if i[2]==1:
                        h[j]+=1
                    else:
                        h[j]-=1
                else:
                    if i[2]==1:
                        h[j]=1
                    else:
                        h[j]=-1
        str1=""
        shi=0
        for i in range(0,len(s)):
            if i in h:
               shi= h[i]
            else:
                shi=0
            original_index = ord(s[i]) - ord('a')
            new_index = (original_index + shi) % 26
            str1+=chr(new_index + ord('a'))
        print(str1)
        


s=Solution()
s.shiftingLetters(  s = "dztz", shifts = [[0,0,0],[1,1,1]])


'''
class Solution(object):
    def shiftingLetters(self, s, shifts):
        """
        :type s: str
        :type shifts: List[List[int]]
        :rtype: str
        """
        # Create a difference array for shifts
        diff = [0] * (len(s) + 1)

        # Apply shifts using the difference array
        for start, end, direction in shifts:
            if direction == 1:
                diff[start] += 1
                if end + 1 < len(s):
                    diff[end + 1] -= 1
            else:
                diff[start] -= 1
                if end + 1 < len(s):
                    diff[end + 1] += 1

        # Compute the actual shifts for each index
        shift_amount = 0
        result = []
        for i in range(len(s)):
            shift_amount += diff[i]
            # Calculate the new character after applying the shift
            original_index = ord(s[i]) - ord('a')
            new_index = (original_index + shift_amount) % 26
            result.append(chr(new_index + ord('a')))
        
        return ''.join(result)

# Example usage
s = Solution()
print(s.shiftingLetters(s = "dztz", shifts = [[0,0,0],[1,1,1]]))  # Should return the correct result

'''