class Solution(object):
    def queryResults(self, limit, queries):
        """
        :type limit: int
        :type queries: List[List[int]]
        :rtype: List[int]
        """
        key_to_value = {}  # Maps each key to its current associated value
        value_count = {}   # Counts how many keys are associated with each value
        result = []        # Stores the count of unique values used by keys

        unique_value_count = 0  # Tracks the count of unique values

        for a, b in queries:
            # If the key `a` has a previous association
            if a in key_to_value:
                prev_value = key_to_value[a]
                if prev_value == b:
                    # If the value remains the same, append current unique value count
                    result.append(unique_value_count)
                    continue

                # Decrease count for the old value
                value_count[prev_value] -= 1
                if value_count[prev_value] == 0:
                    unique_value_count -= 1

            # Set the new association
            key_to_value[a] = b

            # Increase count for the new value
            if b in value_count:
                value_count[b] += 1
            else:
                value_count[b] = 1

            if value_count[b] == 1:
                unique_value_count += 1

            # Append the current count of unique values
            result.append(unique_value_count)

        return result

s = Solution()
print(s.queryResults(limit=1, queries=[[0, 1], [0, 4], [1, 2], [1, 5], [1, 4]]))  # Output: [1, 1, 2, 2, 1]
