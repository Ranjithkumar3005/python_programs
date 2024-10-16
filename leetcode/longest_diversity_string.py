import heapq


class Solution(object):
    def longestDiverseString(self, a, b, c):
        """
        :type a: int
        :type b: int
        :type c: int
        :rtype: str
        """
        max_heap = []
        if a > 0:
            heapq.heappush(max_heap, (-a, "a"))
        if b > 0:
            heapq.heappush(max_heap, (-b, "b"))
        if c > 0:
            heapq.heappush(max_heap, (-c, "c"))

        result = []
        while max_heap:
            count, char = heapq.heappop(max_heap)

            # Check if the last two characters are the same as the current character
            if len(result) >= 2 and result[-1] == result[-2] == char:
                # If no other character is available, break out
                if not max_heap:
                    break

                # Use the next most frequent character instead
                second_count, second_char = heapq.heappop(max_heap)
                result.append(second_char)
                second_count += 1  # increase as count is negative
                if second_count != 0:
                    heapq.heappush(max_heap, (second_count, second_char))

                # Put the original character back into the heap
                heapq.heappush(max_heap, (count, char))
            else:
                # Append current character if no restriction
                result.append(char)
                count += 1
                if count != 0:
                    heapq.heappush(max_heap, (count, char))

        return "".join(result)


# Example usage
s = Solution()
print(s.longestDiverseString(a=1, b=1, c=7))
