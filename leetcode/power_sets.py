n = int(input())
nums = list(map(int, input().split()))
nums = nums[::-1]
result = [[nums[0]]]
c = 1
while c != len(nums):
    result.append([nums[c]])
    for i in range(0, len(result) - 1):
        result.append([nums[c]] + result[i])
    c += 1
for subset in result:
    print(" ".join(map(str, subset)))
