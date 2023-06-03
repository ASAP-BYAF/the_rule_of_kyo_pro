n = int(input())
capacity_list = list(map(int, input().split()))
l_max_capacity_list = []
r_max_capacity_list = []

l_max_tmp = 0
for i, i_cap in enumerate(capacity_list[:n-2]):
    l_max_tmp = max(l_max_tmp, i_cap)
    l_max_capacity_list.append(l_max_tmp)

r_max_tmp = 0
for i, i_cap in enumerate(capacity_list[n-1:1:-1]):
    r_max_tmp = max(r_max_tmp, i_cap)
    r_max_capacity_list.append(r_max_tmp)

d = int(input())
for _ in range(d):
    l, r = map(int, input().split())
    l -= 2
    r = (n-1) - r
    print(max(l_max_capacity_list[l], r_max_capacity_list[r]))