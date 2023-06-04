import sys

# 再帰呼び出しの深さの上限を 120000 に設定
sys.setrecursionlimit(120000)

def dfs_func(g, v, v_connected):
    """ グラフ g において頂点 v からみて連結かどうかを判定します。
    Args:
        g (list[set[int]]): 隣接リスト
        v (int): 探索を開始する頂点
        v_connected (list[int]): 現時点で連結な頂点の集合を返します。

    Returns:
        None: g の v から見た時に到達できるかの論理値のリスト 
            v_conneted (list[logical]) を更新します。
    """
    
    v_connected[v-1] = True
    for i_adj in g[v]:
        if not v_connected[i_adj-1]:
            dfs_func(g, i_adj, v_connected)

n,m = map(int, input().split())
graph = [set() for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].add(b)
    graph[b].add(a)

visited = [False for _ in range(n)]
dfs_func(graph, 1, visited)
    
if all(visited):
    print("The graph is connected.")
else:
    print("The graph is not connected.")
    