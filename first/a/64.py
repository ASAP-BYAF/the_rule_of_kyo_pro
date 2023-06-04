n,m = map(int, input().split())
graph = [set() for _ in range(n+1)]
for _ in range(m):
    a, b, w = map(int, input().split())
    graph[a].add((b, w))
    graph[b].add((a, w))

dist = [1.0e+10 for i in range(n+1)]
dist[1] = 0
v_visited = [1]

while True:
    min_dist = 1.0e+20
    for i in v_visited:
        for v, w in graph[i]:
            if dist[v] > 1.0e+9:
                dist_nex = dist[i] + w
                if dist_nex < min_dist:
                    min_dist = dist_nex
                    min_v = v
                    v_visited.append(min_v)
    if min_dist > 1.0e+15:
        break
    else:
        dist[min_v] = min_dist

for i_dist in dist[1:]:
    print(i_dist)
