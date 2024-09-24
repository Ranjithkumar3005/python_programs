import math


# Function to check if a number is prime
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True


def sort_string(S):
    prime_chars = []
    composite_chars = []

    # Classify characters based on their ASCII values
    for char in S:
        ascii_val = ord(char)
        if is_prime(ascii_val):
            prime_chars.append(char)
        else:
            composite_chars.append(char)

    # Sort prime characters by ascending ASCII value
    prime_chars.sort(key=lambda x: ord(x))

    # Sort composite characters by descending ASCII value
    composite_chars.sort(key=lambda x: ord(x), reverse=True)

    # Concatenate the sorted characters
    return "".join(prime_chars + composite_chars)


# Input handling
N = int(input())  # Length of string (Not used but part of input format)
S = input()  # The string to be sorted

# Output the sorted string
print(sort_string(S))
