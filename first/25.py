h, w = map(int, input().split())
route = []
for i in range(h):
    route.append(input())

dp = [[0 for _ in range(w+1)] for _ in range(h+1)]

# スタート地点は最初から 1 通りの行き方がある。
dp[1][1] = 1

for i_h in range(1,h+1):
    for i_w in range(1,w+1):
        if i_h * i_w != 1 and route[i_h-1][i_w-1] != '#':
            dp[i_h][i_w] = dp[i_h-1][i_w] + dp[i_h][i_w-1]

print(dp[h][w])