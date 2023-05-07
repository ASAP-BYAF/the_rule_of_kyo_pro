h, w, n = map(int,input().split())
amount_of_snow = [[0 for i in range(w+2)] for i in range(h+2)]

for _ in range(n):
    a, b, c, d = map(int, input().split())
    amount_of_snow[a][b] += 1
    amount_of_snow[c+1][d+1] += 1
    amount_of_snow[a][d+1] -= 1
    amount_of_snow[c+1][b] -= 1

for i_h in range(1,h+1):
    for i_w in range(1, w+1):
        amount_of_snow[i_h][i_w] += amount_of_snow[i_h][i_w-1]

for i_h in range(1, h+1):
    for i_w in range(1, w+1):
        amount_of_snow[i_h][i_w] += amount_of_snow[i_h-1][i_w]
        print(amount_of_snow[i_h][i_w], end=' ')
    print('') # 行が変わるごとに改行
