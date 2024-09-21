# cook your dish here
def can_tomu_win(A, K):
    n = len(A)
    
    # Split into picks for Motu and Tomu
    motu_picks = [A[i] for i in range(0, n, 2)]
    tomu_picks = [A[i] for i in range(1, n, 2)]
    
    # Sort picks
    motu_picks.sort(reverse=True)  # Ascending order
    tomu_picks.sort()  # Descending order
    
    # Initial scores
    motu_score = sum(motu_picks)
    tomu_score = sum(tomu_picks)
    
    # Perform at most K swaps
    swaps = 0
    for i in range(min(len(tomu_picks), len(motu_picks))):
        if swaps < K and tomu_picks[i] < motu_picks[i]:
            # Perform a swap
            tomu_score +=  motu_picks[i]-tomu_picks[i]   # Increase Tomu's score
            motu_score +=  tomu_picks[i]-motu_picks[i]   # Decrease Motu's score
            swaps += 1
    
    # Determine if Tomu can win
    return tomu_score > motu_score

# Example usage
T = int(input())
for _ in range(T):
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    result = can_tomu_win(A, K)
    print("Yes" if result else "No")
