def count_distinct_excluding_range(A, L, R):
    # Create a set of all elements in the array
    full_set = set(A)
    
    # Create a set for elements within the range [L, R]
    excluded_set = set(A[L:R+1])
    
    # Return the count of distinct elements in the remaining part
    return len(full_set - excluded_set)

def main():
    pass

if __name__ == "__main__":
    main()
