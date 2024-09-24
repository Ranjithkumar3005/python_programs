from itertools import combinations


# Helper function to generate all possible numbers after deleting digits
def generate_all_numbers(num):
    num_str = str(num)
    length = len(num_str)
    results = set()

    # Generate all subsets by deleting digits
    for i in range(1, length + 1):
        for combo in combinations(num_str, i):
            # Convert the tuple of digits back to an integer
            results.add(int("".join(combo)))

    return results


def find_unique_xor_pairs(x, y):
    # Generate all possible numbers for X and Y
    x_subsets = generate_all_numbers(x)
    y_subsets = generate_all_numbers(y)
    print(x_subsets)
    print(y_subsets)

    # Find pairs where XOR is 0 and store unique pairs
    unique_pairs = set()
    for x_val in x_subsets:
        for y_val in y_subsets:
            if x_val ^ y_val == 0:
                unique_pairs.add((x_val, y_val))

    return unique_pairs


# Main function to handle test cases
def process_test_cases():
    T = int(input())  # Number of test cases
    for _ in range(T):
        X, Y = map(int, input().split())
        unique_pairs = find_unique_xor_pairs(X, Y)

        # Output the result
        print(len(unique_pairs))


# Sample Input: Number of test cases followed by pairs of X and Y
process_test_cases()
