n,m = map(int, input().split())
graph = [set() for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].add(b)
    graph[b].add(a)

for i, i_adj in enumerate(graph[1:n+1],1):
    if i_adj:
        print(f'{i}: {i_adj}')
    else:
        print(f'{i}: {{}}')