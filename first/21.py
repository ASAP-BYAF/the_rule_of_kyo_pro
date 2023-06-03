n = int(input())

p = [0 for i in range(n+2)]
a = [0 for i in range(n+2)]

for i in range(1,n+1):
    p[i], a[i] = map(int, input().split())

dp = [[0 for _ in range(n+2)] for _ in range(n+2)]

for i in range(1,n):
    for left in range(1,i+2):
        right = left + (n-i-1)
        from_left = dp[left-1][right]
        from_right = dp[left][right+1]
        if left <= p[left-1] <= right:
            from_left += a[left-1]
        if left <= p[right+1] <= right:
            from_right += a[right+1]
        dp[left][right] = max(from_left, from_right)

ans = 0
for i in range(1,n+1):
    ans = max(ans, dp[i][i])
print(ans)