class Solution(object):
    def getFolderNames(self, names):
        """
        :type names: List[str]
        :rtype: List[str]
        """
        name_count = {}
        result = []

        for name in names:
            if name not in name_count:
                result.append(name)
                name_count[name] = 0
            else:
                k = name_count[name] + 1
                new_name = f"{name}({k})"
                while new_name in name_count:
                    k += 1
                    new_name = f"{name}({k})"
                result.append(new_name)
                name_count[new_name] = 0
                name_count[name] = k

        return result

# Example usage:
s = Solution()
print(s.getFolderNames(names = ["gta","gta(1)","gta","avalon"]))  # Output should be ["gta", "gta(1)", "gta(2)", "avalon"]
