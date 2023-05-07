h, w = map(int, input().split())
population_sum_list = [[0 for i in range(w+1)] for i in range(h+1)]
for i_h in range(1,h+1):
    population_list = list(map(int, input().split()))

    sum_tmp = 0
    for i_w, i_pop in enumerate(population_list, 1):
        sum_tmp += i_pop
        population_sum_list[i_h][i_w] = sum_tmp

for i_h in range(1, h+1):
    for i_w in range(1, w+1):
        population_sum_list[i_h][i_w] += population_sum_list[i_h-1][i_w]

q = int(input())

for i_q in range(q):
    a, b, c, d = map(int, input().split())
    print(population_sum_list[c][d] - population_sum_list[a-1][d]
        + population_sum_list[a-1][b-1] - population_sum_list[c][b-1])
