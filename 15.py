n = input()
a = list(map(int, input().split()))

a_sorted = sorted(list(set(a)))

dict = {}
for i, i_a in enumerate(a_sorted):
    dict[i_a] = i

# print(dict)

for i in a:
    print(dict[i]+1, end=' ')

print('')
