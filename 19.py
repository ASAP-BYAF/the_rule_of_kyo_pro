n, w = map(int, input().split())
item_list = []
for _ in range(n):
    item_list.append(list(map(int, input().split())))

w_max = w+1
n_max = n+1
dp = [[0 for _ in range(w_max)] for _ in range(n_max)]

for j, (j_w, j_v) in enumerate(item_list):
    for i, i_dp in enumerate(dp[j]):
        if i_dp :
            if i+j_w < w_max:
                dp[j+1][i+j_w] = max(dp[j][i+j_w], dp[j][i] + j_v)
            dp[j+1][i] = max(dp[j+1][i], dp[j][i])
    dp[j+1][j_w] = max(dp[j+1][j_w], j_v)

for i in dp[n][::-1]:
    if i:
        print(i)
        break