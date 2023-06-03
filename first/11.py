def bi_search_func(x, target):
    x_sorted = sorted(x)
    left = 0
    right = len(x) - 1

    while left <= right:
        mid = (left + right) // 2

        if x_sorted[mid] == target:
            return mid

        elif x_sorted[mid] > target:
            right = mid - 1

        elif x_sorted[mid] < target:
            left = mid + 1

n, x = map(int, input().split())
num_list = list(map(int,input().split()))
index = bi_search_func(num_list, x)
print(index+1)