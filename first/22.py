n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
dp = [0 for _ in range(n)]

for i in range(n-1):
    if i == 0:
        dp[a[i]-1] = max(dp[a[i]-1], dp[i]+100)
        dp[b[i]-1] = max(dp[b[i]-1], dp[i]+150)
    else:
        if dp[i] > 0:
            dp[a[i]-1] = max(dp[a[i]-1], dp[i]+100)
            dp[b[i]-1] = max(dp[b[i]-1], dp[i]+150)

print(dp[n-1])