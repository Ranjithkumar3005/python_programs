def longest_sorted_prefix(A, queries):
    N = len(A)
    prefix_length = [0] * N  # Initialize prefix_length array
    current_length = 0

    # Preprocess to find the initial longest sorted prefix
    for i in range(1, N):
        if A[i] >= A[i - 1]:
            current_length += 1
        else:
            current_length = 0
        prefix_length[i] = current_length

    # Handle queries
    results = []
    for query in queries:
        index = query
        # Update prefix_length for the removed element and its successor
        if index > 0:
            prefix_length[index - 1] = max(prefix_length[index - 1] - 1, 0)
        if index < N - 1:
            prefix_length[index] = max(prefix_length[index] - 1, 0)
            if A[index] >= A[index - 1]:
                prefix_length[index] = prefix_length[index - 1] + 1

        # Find the new longest sorted prefix
        longest = 0
        for i in range(N):
            longest = max(longest, prefix_length[i])
        results.append(longest)

    return results

# Example usage
A = [1, 2, 5, 3, 4]
X = [3, 2,1,0,4]
result = longest_sorted_prefix(A, X)
print(result) 
