n = int(input())
capacity_list = list(map(int, input().split()))
capacity_list = [0] + capacity_list # 先頭に 0 を追加(引数は 0)
# capacity_list.append(0) # 末尾に 0 を追加(引数は n+1)
max_capacity_list = [[0 for _ in range(n)] for _ in range(n)]

for i_l in range(2,n):
    for i_r in range(i_l,n):
        # print(i_l, i_r)
        # print(f'left = {capacity_list[:i_l+1]}right = {capacity_list[:i_r-1:-1]}')
        max_capacity_list[i_l][i_r] = max(max(capacity_list[:i_l]), max(capacity_list[:i_r:-1]))

# print(max_capacity_list)

d = int(input())
for _ in range(d):
    l, r = map(int, input().split())
    print(max_capacity_list[l][r])