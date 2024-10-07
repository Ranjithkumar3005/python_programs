class Solution(object):
    def tictactoe(self, moves):
        """
        :type moves: List[List[int]]
        :rtype: str
        """
        ar, ac = {}, {}
        br, bc = {}, {}  # Rows and columns for player B
        ad, bd = [0, 0], [0, 0]  # Diagonals for players A and B
        check = True
        for i in moves:
            if check:
                check = False
                ar[i[0]] = ar.get(i[0], 0) + 1
                ac[i[1]] = ac.get(i[1], 0) + 1
                if i[0] == i[1]:  # Left-to-right diagonal
                    ad[0] += 1
                if i[0] + i[1] == 2:  # Right-to-left diagonal
                    ad[1] += 1

                if ar[i[0]] == 3 or ac[i[1]] == 3 or ad[0] == 3 or ad[1] == 3:
                    return "A"
            else:
                check = True
                br[i[0]] = br.get(i[0], 0) + 1
                bc[i[1]] = bc.get(i[1], 0) + 1
                if i[0] == i[1]:  # Left-to-right diagonal
                    bd[0] += 1
                if i[0] + i[1] == 2:  # Right-to-left diagonal
                    bd[1] += 1
                if br[i[0]] == 3 or bc[i[1]] == 3 or bd[0] == 3 or bd[1] == 3:
                    return "B"

        if len(moves) == 9:
            return "Draw"
        else:
            return "Pending"


# Example usage
s = Solution()
print(s.tictactoe(moves=[[0, 0], [2, 0], [1, 1], [2, 1], [2, 2]]))  # Output: "A"
