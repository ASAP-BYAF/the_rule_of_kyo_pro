import math

def bi_search_func(interval_list, goal_amount):
    left = 1
    right = goal_amount * max(interval_list)
    # right = goal_amount
    first_time = right
    while left <= right:

        mid = (left + right) // 2
        total = 0
        for i_interval in interval_list:
            total += mid // i_interval

        if total >= goal_amount:
            first_time = min(first_time, mid)
            right = mid - 1

        elif total < goal_amount:
            left = mid + 1

    return first_time

n, k = map(int, input().split())
print_interval_list = list(map(int, input().split()))
y = bi_search_func(print_interval_list,k)
print(y)