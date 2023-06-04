n,m = map(int, input().split())
graph = [set() for _ in range(n+1)]
for _ in range(m):
    a, b, w = map(int, input().split())
    graph[a].add((b, w))
    graph[b].add((a, w))

dist = [1.0e+10 for i in range(n+1)]
dist[1] = 0

while True:
    min_dist = 1.0e+20
    for i, i_dist in enumerate(dist[1:], 1):
        if i_dist < 1.0e+9:
            for v, w in graph[i]:
                if dist[v] > 1.0e+9:
                    if i_dist + w < min_dist:
                        min_dist = i_dist + w
                        min_v = v
    if min_dist > 1.0e+15:
        break
    else:
        dist[min_v] = min_dist

for i_dist in dist[1:]:
    print(i_dist)
