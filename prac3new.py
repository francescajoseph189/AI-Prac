import heapq

start = (1,2,3,4,0,6,7,5,8)
goal = (1,2,3,4,5,6,7,8,0)

def h(s):
    return sum(abs(i//3-(v-1)//3)+abs(i%3-(v-1)%3)
               for i,v in enumerate(s) if v)

q = [(h(start), 0, start, [])]
visited = set()

while q:
    f,g,s,path = heapq.heappop(q)
    if s in visited: continue
    visited.add(s)
    path += [s]

    if s == goal:
        for x in path:
            print(x[:3]); print(x[3:6]); print(x[6:]); print()
        print("Goal Reached!")
        break

    z = s.index(0)

    for d in [-3,3,-1,1]:
        n = z+d
        if not 0 <= n < 9 or (d == -1 and z%3 == 0) or (d == 1 and z%3 == 2):
            continue

        a = list(s)
        a[z],a[n] = a[n],a[z]
        a = tuple(a)

        if a not in visited:
            heapq.heappush(q,(g+1+h(a),g+1,a,path))