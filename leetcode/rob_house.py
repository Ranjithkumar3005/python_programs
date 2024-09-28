import math

# Function to determine if Charlie can rob all houses in H hours with speed K
def can_rob_all_houses(K, houses, H):
    total_hours = 0
    for house_count in houses:
        total_hours += math.ceil(house_count / K)
    return total_hours <= H

# Main function to find the minimum K
def min_robbing_speed(N, H, houses):
    # Binary search between 1 and max(houses)
    left, right = 1, max(houses)
    
    while left < right:
        mid = (left + right) // 2
        if can_rob_all_houses(mid, houses, H):
            right = mid  # Try to minimize K
        else:
            left = mid + 1  # Increase K

    return left

# Input reading
if __name__ == "__main__":
    N, H = map(int, input().split())
    houses = list(map(int, input().split()))
    
    # Output the minimum K
    print(min_robbing_speed(N, H, houses))
