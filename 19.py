n, w = map(int, input().split())
item_list = []
for _ in range(n):
    item_list.append(list(map(int, input().split())))

w_max = w+1
n_max = n+1
# dp = [[0 for _ in range(w_max)] for _ in range(n_max)]
dp = [[-1.0e+10 for _ in range(w_max)] for _ in range(n_max)]
dp[0][0] = 0

for j, (j_w, j_v) in enumerate(item_list):
    for i, i_dp in enumerate(dp[j]):
        if i < j_w: 
            dp[j+1][i]= dp[j][i]
        else:
            dp[j+1][i] = max(dp[j][i], dp[j][i-j_w] + j_v)

print(max(dp[n]))