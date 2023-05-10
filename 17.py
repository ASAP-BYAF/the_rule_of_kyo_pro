# 入力を受け取る
n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

# 初期処理
min_time = [0 for _ in range(n)]
min_time[1] = a[0]

for i in range(2, n):
    min_time[i] = min(min_time[i-1] + a[i-1], min_time[i-2] + b[i-2])

path = [n-1]
current_place = n-1
num_place = 1
while current_place > 0:

    # 現在までの最短経路の直前が一つ前の部屋の時
    if min_time[current_place] == min_time[current_place-1] + a[current_place-1]:
        current_place -= 1

    # 現在までの最短経路の直前が二つ前の部屋の時
    elif min_time[current_place] == min_time[current_place-2] + b[current_place-2]:
        current_place -= 2

    num_place += 1
    path.append(current_place)

print(num_place)
path_str = [str(i+1) for i in path[::-1]]
print(' '.join(path_str))

