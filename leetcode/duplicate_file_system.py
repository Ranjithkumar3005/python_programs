class Solution:
    def findDuplicate(self, paths):
        h = {}
        for i in paths:
            arr = i.split(" ")
            path = arr[0]
            for j in range(1, len(arr)):
                inx = arr[j].index("(")
                val = arr[j][inx:]
                tot = path + "/" + arr[j][:inx]
                if val not in h:
                    h[val] = [tot]
                else:
                    h[val].append(tot)
        dum2 = []
        for i in h:
            dum2.append(h[i])
        print(dum2)


s = Solution()
s.findDuplicate(
    paths=[
        "root/a 1.txt(abcd) 2.txt(efgh)",
        "root/c 3.txt(abcd)",
        "root/c/d 4.txt(efgh)",
        "root 4.txt(efgh)",
    ]
)
