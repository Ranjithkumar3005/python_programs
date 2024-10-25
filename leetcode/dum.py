from collections import deque


def min_rook_moves(board):
    # Convert 1-based indexing to 0-based
    n = 8
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # up, down, left, right

    # Locate the rook
    for i in range(n):
        for j in range(n):
            if board[i][j] == "R":
                start = (i, j)

    # BFS
    queue = deque([(start[0], start[1], 0)])  # (x, y, moves)
    visited = set()
    visited.add(start)

    while queue:
        x, y, moves = queue.popleft()

        # If we reach the destination (7, 7 in 0-based index)
        if x == 7 and y == 7:
            return moves

        # Explore all 4 directions
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            while (
                0 <= nx < n and 0 <= ny < n and board[nx][ny] == "B"
            ):  # Move in the current direction
                if (nx, ny) not in visited:
                    visited.add((nx, ny))
                    queue.append((nx, ny, moves + 1))
                nx += dx
                ny += dy

    # If we exhaust the BFS and don't reach (7, 7), return -1
    return -1


# Example usage
board = [
    ["B", "B", "B", "B", "B", "B", "B", "B"],
    ["B", "P", "B", "P", "B", "P", "B", "B"],
    ["B", "B", "B", "B", "B", "P", "B", "B"],
    ["B", "B", "B", "P", "B", "B", "B", "B"],
    ["B", "B", "B", "B", "B", "B", "B", "B"],
    ["B", "B", "B", "B", "B", "B", "B", "B"],
    ["B", "B", "B", "P", "B", "P", "B", "B"],
    ["B", "B", "B", "B", "B", "B", "B", "R"],
]

print(min_rook_moves(board))  # Output should be the minimum moves or -1 if impossible
