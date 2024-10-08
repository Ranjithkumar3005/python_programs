class Solution(object):
    def invalidTransactions(self, transactions):
        """
        :type transactions: List[str]
        :rtype: List[str]
        """
        
        r = {}
                
        inv = []        
        for i in transactions:
            split = i.split(",")
            name = str(split[0])
            time = int(split[1])
            amount = int(split[2])
            city = str(split[3])
            
            if time not in r:
                r[time] = {
                    name: [city]
                }
            else:
                if name not in r[time]:
                    r[time][name]=[city]
                else:
                    r[time][name].append(city)
                    
        print(r)
        for i in transactions:
            split = i.split(",")
            name = str(split[0])
            time = int(split[1])
            amount = int(split[2])
            city = str(split[3])
            
            
            if amount > 1000:
                inv.append(i)
                continue
            
            for j in range(time-60, time+61):
                if j not in r:
                    continue
                if name not in r[j]:
                    continue
                if len(r[j][name]) > 1 or (r[j][name][0] != city):
                    inv.append(i)
                    break
                                        
        return inv       
s = Solution()
print(s.invalidTransactions(transactions = ["alice,20,800,mtv", "alice,50,1200,mtv"]))
