def reverse_message(input1: str) -> str:
    # Initialize the dictionary with character flips
    flip_map = {chr(i): chr(219 - i) for i in range(ord('a'), ord('z') + 1)}
    
    # Build the decoded message using the flip_map
    decoded_message = ''.join(flip_map[ch] for ch in input1)
    
    return decoded_message

# Example usage
input_string = "zhvw"
print(reverse_message(input_string))  # Output: "asex"



# def decode_message(message: str) -> str:
#     decoded_message = []
    
#     for ch in message:
#         position = ord(ch) - ord('a')
#         opposite_position = 25 - position
#         opposite_char = chr(ord('a') + opposite_position)
#         decoded_message.append(opposite_char)
    
#     return ''.join(decoded_message)

# # Example usage
# input_string = "zhvw"
# print(decode_message(input_string))  # Output: "zyxdef"
