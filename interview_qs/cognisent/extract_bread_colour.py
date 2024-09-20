def find_bread_colors(input_str: str) -> str:
    breads = []
    n = len(input_str)
    is_bread = [False] * n
    
    for i in range(n):
        if not is_bread[i]:
            bread = input_str[i]
            for j in range(i + 1, n):
                if input_str[j] == bread:
                    # Mark all positions from i to j as bread
                    for k in range(i, j + 1):
                        is_bread[k] = True
                    breads.append(bread)
                    break
    
    return ''.join(breads)

# Example usage
input_string = "qczcquu"
print(find_bread_colors(input_string))  # Output: "qu"
