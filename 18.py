import sys

n, s = map(int, input().split())
a_list = list(map(int, input().split()))

sum_set = {0}
for a_i in a_list:
    sum_set_tmp = set()
    for sum_i in sum_set:
        sum_set_tmp.add(sum_i + a_i)
    sum_set = sum_set | sum_set_tmp
    
    if s in sum_set:
        print('Yes')
        sys.exit()
print('No')