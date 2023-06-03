n, q = map(int, input().split())
population_list = list(map(int, input().split()))
population_sum_list = [0]

sum_tmp = 0
for i in population_list:
    sum_tmp += i
    population_sum_list.append(sum_tmp)


for i in range(q):
    l, r = map(int, input().split())
    print(population_sum_list[r] - population_sum_list[l-1])

