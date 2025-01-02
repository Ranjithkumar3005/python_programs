def maxSum(arr, k):
    left = 0
    max1 = sum(arr[:k])
    for i in range(k, len(arr)):
        max2 = max1 - arr[left] + arr[i]
        max1 = max(max1, max2)
        max1 = max2
        left += 1
    return max1

print(maxSum(arr=[1, 2, 3, 4, 5], k=3))
#