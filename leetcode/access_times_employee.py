class Solution(object):
    def findHighAccessEmployees(self, access_times):
        """
        :type access_times: List[List[str]]
        :rtype: List[str]
        """
        h = {}
        for i in access_times:
            if i[0] in h:
                val1 = int(i[1][:2]) * 60
                val1 += int(i[1][2:])
                h[i[0]].append(val1)
            else:
                val1 = int(i[1][:2]) * 60
                val1 += int(i[1][2:])
                h[i[0]] = [val1]
        dum = []
        for i in h:
            val = h[i]
            val = sorted(val)
            for k in range(0, len(val) - 2):
                if val[k] + 60 > val[k + 2]:
                    dum.append(i)
                    break
        print(dum)
        return dum


s = Solution()
s.findHighAccessEmployees(
    access_times=[
        ["d", "0002"],
        ["c", "0808"],
        ["c", "0829"],
        ["e", "0215"],
        ["d", "1508"],
        ["d", "1444"],
        ["d", "1410"],
        ["c", "0809"],
    ]
)
