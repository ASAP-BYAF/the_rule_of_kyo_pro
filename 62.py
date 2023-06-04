def dfs_func(g, v, v_connected):
    """ グラフ g において頂点 v からみて連結かどうかを判定します。
    Args:
        g (list[set[int]]): 隣接リスト
        v (int): 探索を開始する頂点
        v_connected (list[int]): 現時点で連結な頂点の集合を返します。

    Returns:
        v_conneted (list[int]): g の v から見た連結成分のリスト
    """
    
    if g[v]:
        for i_adj in g[v]:
            if not i_adj in v_connected:
                v_connected.append(i_adj)
                dfs_func(g, i_adj, v_connected)

n,m = map(int, input().split())
graph = [set() for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].add(b)
    graph[b].add(a)

connected_component = []
dfs_func(graph, 1, connected_component)
    
if len(connected_component) == n:
    print("The graph is connected.")
else:
    print("The graph is not connected.")
    