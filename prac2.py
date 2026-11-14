
# Model-Based Intelligent Agent

grid = [
    [0, 0, 0, 0],
    [0, 1, 1, 0],
    [0, 0, 0, 0],
    [0, 1, 0, 0]
]

position = (0, 0)
goal = (3, 3)
visited = []

while position != goal:
    visited.append(position)
    x, y = position

    if y < 3 and grid[x][y + 1] == 0:
        position = (x, y + 1)
    elif x < 3 and grid[x + 1][y] == 0:
        position = (x + 1, y)
    elif y > 0 and grid[x][y - 1] == 0:
        position = (x, y - 1)
    elif x > 0 and grid[x - 1][y] == 0:
        position = (x - 1, y)
    else:
        print("No path found!")
        break

    print("Current Position:", position)

print("Goal Reached:", position == goal)
