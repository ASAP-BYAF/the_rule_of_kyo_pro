n, q = map(int, input().split())

root_list = [0 for i in range(n+1)]
for _ in range(q):
    num, u, v = map(int, input().split())

    if num == 1:
        u_root = root_list[u]
        v_root = root_list[v]
        if not u_root and not v_root:
            root_list[u] = u
            root_list[v] = u
        elif not v_root:
            root_list[v] = u_root
        elif not u_root:
            root_list[u] = v_root
        else:
            root_list[v_root] = u_root
            for i, i_root in enumerate(root_list):
                if i_root == v_root:
                    root_list[i] = u_root
    else:
        u_root = root_list[u]
        v_root = root_list[v]
        if v_root*u_root != 0 and v_root == u_root:
            print('Yes')
        else:
            print('No')
