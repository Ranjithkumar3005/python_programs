def isRobotBounded(instructions):
    # Initial position and direction (facing north)
    x, y = 0, 0
    direction = 0  # 0: North, 1: East, 2: South, 3: West

    # Directions as (dx, dy) for North, East, South, West
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    # Execute each instruction
    for instruction in instructions:
        if instruction == "G":
            dx, dy = directions[direction]
            x += dx
            y += dy
        elif instruction == "L":
            direction = (direction - 1) % 4
        elif instruction == "R":
            direction = (direction + 1) % 4

    # Check if the robot is bounded
    # Bounded if back at origin or facing a different direction than north
    return (x == 0 and y == 0) or direction != 0
