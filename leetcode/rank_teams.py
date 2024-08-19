class Solution(object):
    def rankTeams(self, votes):
        """
        :type votes: List[str]
        :rtype: str
        """
        # Initialize the dictionary to store rank counts
        h = {}
        for i in votes:
            for j in range(len(i)):
                if i[j] not in h:
                    h[i[j]] = [0] * len(i)
                h[i[j]][j] += 1
        
        print(h)
        sorted_teams = sorted(h.keys(), key=lambda team: (h[team], team), reverse=True)
        
        result = ''.join(sorted_teams)
        return result

s = Solution()
print(s.rankTeams(votes = ["ABC", "ACB", "ABC", "ACB", "ACB"]))  # Output should be "ACB"
