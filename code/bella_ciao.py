def check(nums):
    c = 0
    rate = nums[2]  # Initial production rate
    for i in range(nums[0]):  # nums[0] is the number of days
        c += rate  # Add current rate to total
        if (i + 1) % nums[1] == 0:  # Check if it's time to increment
            rate += nums[3]  # Increment the rate by Q
    print(c)

T = int(input())
for _ in range(T):
    A = list(map(int, input().split()))
    check(A)
