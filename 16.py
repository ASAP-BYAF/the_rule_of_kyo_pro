# 入力を受け取る
n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

# 初期処理
min_time = [0 for _ in range(n)]
min_time[1] = a[0]

for i in range(2, n):
    min_time[i] = min(min_time[i-1] + a[i-1], min_time[i-2] + b[i-2])

print(min_time[-1])