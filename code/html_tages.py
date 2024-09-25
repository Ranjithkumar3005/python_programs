def check(N):
    # Check if the string is long enough
    N = N.strip()
    if len(N) < 4:
        print("Error")
        return

    # Check for proper opening and closing tag format
    val1 = N[:2]
    if val1 != "</":
        print("Error")
        return
    val2 = N[len(N) - 1]
    if val2 != ">":
        print("Error")
        return

    tag_content = N[2:-1]  # Get content without '<' and '>'
    if len(tag_content) == 0:
        print("Error")
        return

    for char in tag_content:
        print(char.islower())
        if char.isalpha():
            if not char.islower():
                print("Error")
                return
        elif not char.isdigit() and not char.isalpha():
            print("Error")
            return

    print("Success")


T = int(input())  # Number of test cases

for _ in range(T):
    N = input()
    check(N)
