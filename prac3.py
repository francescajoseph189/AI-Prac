
# A* Search for 8-Puzzle

import heapq

start = (1, 2, 3, 4, 0, 6, 7, 5, 8)
goal = (1, 2, 3, 4, 5, 6, 7, 8, 0)

def h(state):
    return sum(abs(i//3 - (v-1)//3) +
               abs(i%3 - (v-1)%3)
               for i, v in enumerate(state) if v != 0)

q = [(h(start), 0, start, [])]
visited = set()

while q:
    f, g, state, path = heapq.heappop(q)

    if state in visited:
        continue
    visited.add(state)

    path = path + [state]

    if state == goal:
        for s in path:
            print(s[:3])
            print(s[3:6])
            print(s[6:])
            print()
        print("Goal Reached!")
        break

    z = state.index(0)

    for d in [-3, 3, -1, 1]:
        n = z + d

        if n < 0 or n > 8:
            continue
        if d == -1 and z % 3 == 0:
            continue
        if d == 1 and z % 3 == 2:
            continue

        new = list(state)
        new[z], new[n] = new[n], new[z]
        new = tuple(new)

        if new not in visited:
            heapq.heappush(q, (g + 1 + h(new),
                               g + 1, new, path))
