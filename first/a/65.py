n = int(input())
a_list = list(map(int, input().split()))

dp = [0 for _ in range(n+1)]

for i, i_a in enumerate(a_list[::-1]):

    # 自身の上司の部下の数は自分の部下と自分の数の分だけ増える。
    dp[i_a] += dp[n-i] + 1

for i in dp[1:]:
    print(i, end=' ')