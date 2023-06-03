n, s = map(int, input().split())
a_list = list(map(int, input().split()))

dp = [[False for _ in range(10001)] for _ in range(61)]
dp[0][0] = True

for i, a_i in enumerate(a_list):
    for j, sum_j in enumerate(dp[i]):
        if sum_j:
            dp[i+1][j] = True
            if j+a_i <=10000:
                dp[i+1][j+a_i] = True
    
if dp[n][s]:
    print('Yes')
else:
    print('No')


