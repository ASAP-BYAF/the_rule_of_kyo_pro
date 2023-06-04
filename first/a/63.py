from collections import deque

n,m = map(int, input().split())
graph = [set() for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].add(b)
    graph[b].add(a)

dist = [-1 for _ in range(n+1)]
dist[0:2] = [0,0]
queue = deque()
queue.append(1)

while len(queue) >=1:
    cur = queue.popleft()
    for i_adj in graph[cur]:
        if dist[i_adj] == -1:
            dist[i_adj] = dist[cur] + 1
            queue.append(i_adj)

for i_len in dist[1:n+1]:
    print(i_len)