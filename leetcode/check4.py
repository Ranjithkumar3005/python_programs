from collections import Counter

def find_combinations(s, words):
    word_length = len(words[0])
    total_length = word_length * len(words)
    word_count = Counter(words)
    result = []

    # Iterate over each possible starting point of the substring
    for i in range(len(s) - total_length + 1):
        # Extract the current substring
        substring = s[i:i + total_length]
        
        # Create a Counter for the current substring
        substring_count = Counter([substring[j:j + word_length] for j in range(0, total_length, word_length)])
        
        # Check if the Counter matches the word count
        if substring_count == word_count:
            result.append(substring)
    
    return result

# Example usage
s = "wordgoodgoodgoodbestword"
words = ["word", "good", "best", "good"]
combinations = find_combinations(s, words)

# Print all valid combinations
if combinations:
    for combo in combinations:
        print(combo)
else:
    print("No valid combinations found")
