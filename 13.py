def bi_search_func(x, target):
    """
    与えられた整数配列 x の中から整数 target 以上の整数のうち
    最小のものの配列の引数を返します。

    :param x:
    :param target:
    :return:
    """
    x_sorted = sorted(x)
    left = 0
    right = len(x) - 1
    counter_min_index = right + 1

    while left <= right:
        mid = (left + right) // 2

        if x_sorted[mid] >= target:
            counter_min_index = min(counter_min_index, mid)
            # print('if')
            # print(f'counter_min_index = {counter_min_index}')
            # print(f'left = {left}')
            # print(f'right = {right}')
            right = mid - 1

        elif x_sorted[mid] < target:
            # print('else')
            # print(f'counter_min_index = {counter_min_index}')
            # print(f'left = {left}')
            # print(f'right = {right}')
            left = mid + 1

    # print(counter_min_index)
    # print(x)
    # print(target, x[counter_min_index])
    return counter_min_index

n, k = map(int, input().split())
num_list = list(map(int, input().split()))

total_num_combi = 0
for i, i_num in enumerate(num_list[:-1],1):
    k_counter = i_num + k
    # print(f' >>> k = {k}, k_counter = {k_counter}')
    total_num_combi += ((n - i) - (bi_search_func(num_list[i:], k_counter) + 1) + 1)
    # print('total_tmp', total_num_combi)
print(total_num_combi)

