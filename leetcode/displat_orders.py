class Solution(object):
    def displayTable(self, orders):
        """
        :type orders: List[List[str]]
        :rtype: List[List[str]]
        """
        h = {}
        food_items = set()

        for i in orders:
            food_items.add(i[2])
            if i[1] not in h:
                h[i[1]] = {i[2]: 1}
            else:
                if i[2] in h[i[1]]:
                    h[i[1]][i[2]] += 1
                else:
                    h[i[1]][i[2]] = 1
        
        # Sort food items alphabetically
        sorted_food_items = sorted(food_items)
        
        # Sort table numbers numerically
        sorted_tables = sorted(h.keys(), key=int)
        
        # Prepare the result table
        result = [["Table"] + sorted_food_items]
        
        # Fill the table with counts
        for table in sorted_tables:
            row = [table]
            for food in sorted_food_items:
                row.append(str(h[table].get(food, 0)))
            result.append(row)
        
        return result

# Example usage
s = Solution()
output = s.displayTable(orders=[["David", "3", "Ceviche"], ["Corina", "10", "Beef Burrito"],
                                ["David", "3", "Fried Chicken"], ["Carla", "5", "Water"],
                                ["Carla", "5", "Ceviche"], ["Rous", "3", "Ceviche"]])

for row in output:
    print(row)
