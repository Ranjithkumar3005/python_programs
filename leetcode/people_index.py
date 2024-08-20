class Solution(object):
    def peopleIndexes(self, favoriteCompanies):
        """
        :type favoriteCompanies: List[List[str]]
        :rtype: List[int]
        """
        def is_subset(dict1, dict2):
            for key, value in dict1.items():
                if key not in dict2 or dict2[key] != value:
                    return False
            return True
        dum=[]
        
        for i in range(0,len(favoriteCompanies)):
            h1={}
            for j in favoriteCompanies[i]:
                if j in h1:
                    h1[j]+=1
                else:
                    h1[j]=1
            dum.append(h1)
        arr=[]
        
        for i in range(0,len(dum)):
            check=True
            for j in range(0,len(dum)):
                if i==j or len(dum[i])>len(dum[j]):
                    continue
                elif is_subset(dum[i],dum[j]):
                    check=False
                    break
            if check:
                arr.append(i)
        print(arr)
s=Solution()
s.peopleIndexes(favoriteCompanies = [["leetcode","google","facebook"],["google","microsoft"],["google","facebook"],["google"],["amazon"]])