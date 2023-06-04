import sys

# 再帰呼び出しの深さの上限を 120000 に設定
sys.setrecursionlimit(120000)

def bfs_func(g, v, dist):
    """ グラフ g において頂点 v からみて連結かどうかを判定します。
    Args:
        g (list[set[int]]): 隣接リスト
        v (int): 探索を開始する頂点
        dist (list[int]): 各頂点への最短距離リスト

    Returns:
        None: dist を更新します。 
    """
    
    connected_cur = []

    for i_adj in g[v]:
        if dist[i_adj] == -1:
            dist[i_adj] = dist[v] + 1
            connected_cur.append(i_adj)
    
    # まだ探索できていない頂点があり、かつ今回到達できた点が存在するとき
    if -1 in dist and connected_cur:
        for i_adj in connected_cur:
            bfs_func(g, i_adj, dist)

n,m = map(int, input().split())
graph = [set() for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].add(b)
    graph[b].add(a)

dist = [-1 for _ in range(n+1)]
dist[0:2] = [0,0]
bfs_func(graph, 1, dist)

for i_len in dist[1:n+1]:
    print(i_len)