d = int(input())
population_ratio_list = [0 for i in range(d+2)]
n = int(input())

for _ in range(n):
    l, r = map(int, input().split())
    population_ratio_list[l] += 1
    population_ratio_list[r+1] -= 1

sum_tmp = 0
for i in population_ratio_list[1:d+1]:
    sum_tmp += i
    print(sum_tmp)