class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        costs=sorted(costs)
        tot=0
        c=0
        for i in costs:
            tot+=i
            if tot>coins:
                break
            c+=1
        return c