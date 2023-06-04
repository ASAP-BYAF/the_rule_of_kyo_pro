import heapq

n,m = map(int, input().split())
graph = [set() for _ in range(n+1)]
for _ in range(m):
    a, b, w = map(int, input().split())
    graph[a].add((b, w))
    graph[b].add((a, w))

visited = [False for i in range(n+1)]
dist = [1.0e+10 for i in range(n+1)]
dist[1] = 0
Q = []
heapq.heappush(Q, (dist[1], 1))

while Q:
    cur = heapq.heappop(Q)[1]
    
    # 最短距離として取り出されて初めて探索済みとする
    if not visited[cur]:
        visited[cur] = True
        
        # 確定した頂点と隣接していて、かつ距離が小さくなるものを更新。
        for v, w in graph[cur]:
            if not visited[v] and dist[v] > dist[cur] + w:
                dist[v] = dist[cur] + w
                heapq.heappush(Q, (dist[v], v))

for i, i_visited in enumerate(visited[1:], 1):
    if i_visited:
        print(dist[i])
    else:
        print(-1)