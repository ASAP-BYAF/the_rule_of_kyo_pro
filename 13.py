# 入力を受け取る
n, k = map(int, input().split())
a = list(map(int, input().split()))

r_before = 1 # 最初は隣と差を考える。
combi_total = 0 # 組み合わせの合計数の初期値
for i_r in range(n):
    for i_c in range(r_before,n):

        if a[i_c] - a[i_r] > k:
            r_before = i_c - 1
            combi_total += r_before - i_r
            break

        elif i_c == n - 1:
            r_before = i_c
            combi_total += r_before - i_r

print(combi_total)