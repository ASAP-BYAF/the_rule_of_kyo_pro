n, k = map(int, input().split())

combi = 0
for i_red in range(1, n+1):
    for i_blue in range(1, n+1):

        if 0 < k - (i_red + i_blue) <= n :
            combi += 1

        else:
            continue

print(combi)
