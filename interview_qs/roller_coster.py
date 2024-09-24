def check(nums, n):
    h = {}
    for i in range(len(nums)):
        h[nums[i]] = i
    swaps = 0

    for i in range(n):
        correct_value = i + 1
        if nums[i] != correct_value:
            correct_index = h[correct_value]
            nums[i], nums[correct_index] = nums[correct_index], nums[i]
            h[nums[correct_index]] = correct_index
            h[nums[i]] = i

            swaps += 1
    print(h, nums)
    print(swaps)


check([2, 1, 5, 3, 4], 5)
