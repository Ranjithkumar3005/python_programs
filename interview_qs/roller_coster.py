def check(nums, n):
    h = {}
    for i in range(len(nums)):
        h[nums[i]] = i
    swaps = 0

    for i in range(len(nums)):
        if nums[i] != i + 1:
            tem = nums[i]
            nums[i] = i + 1
            nums[h[i + 1]] = tem
            swaps += 1
    print(nums)
    print(swaps)


check([2, 1, 5, 3, 4], 5)
