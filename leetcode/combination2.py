class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        candidates.sort()
        dum = []
        def find_combinations(start, target, path):
            for i in range(start, len(candidates)):
                if i > start and candidates[i] == candidates[i - 1]:
                    continue  # Skip duplicates
                if candidates[i] > target:
                    break  # No need to continue if the candidate exceeds the target
                if candidates[i] == target:
                    dum.append(path + [candidates[i]])
                    break  # No need to continue further as we found a valid combination
                find_combinations(i + 1, target - candidates[i], path + [candidates[i]])

        find_combinations(0, target, [])
        return dum

s = Solution()
output = s.combinationSum2(candidates=[10, 1, 2, 7, 6, 1, 5], target=8)
print(output)
