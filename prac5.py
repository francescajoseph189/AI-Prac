
# BFS for Robot Path Planning

from collections import deque

grid = [
    [0, 0, 0],
    [1, 1, 0],
    [0, 0, 0]
]

start = (0, 0)
goal = (2, 2)

q = deque([(start, [start])])
visited = {start}

while q:
    pos, path = q.popleft()

    if pos == goal:
        print("Path:", path)
        break

    x, y = pos

    for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
        nx, ny = x + dx, y + dy
        next_pos = (nx, ny)

        if (0 <= nx < 3 and 0 <= ny < 3
            and grid[nx][ny] == 0
            and next_pos not in visited):

            visited.add(next_pos)
            q.append((next_pos, path + [next_pos]))
