def binary_search_func(x, y):
    """集合と値を受け取って、その値を集合に入れて昇順にした時の引数を返します。

    Args:
        x (set[int]): 整数値の集合
        y (int): x に入れることを考える整数

    Returns:
        int: y を x に入れた場合何番目に大きいかを返します。
    """

    len_x = len(x)
    x.add(y)
    x_ = sorted(x)

    left = 0 
    right = len(x_)-1

    while left <= right:
        mid = int((left+right)/2)   
        
        if y < x_[mid]:
            right = mid - 1

        elif y > x_[mid]:
            left = mid + 1

        else:
            break
    
    # 受け取った時から長さが y 分増えているときは
    # y は新たに加えたことになるので取り除く。
    if len_x == len(x) - 1:
        x.remove(y)
    return mid

q = int(input())

my_set = set()

for _ in range(q):
    num, value = map(int,input().split())

    if num == 1:
        my_set.add(value)
    elif num == 2:
        my_set.remove(value)
    elif num == 3:
        order = binary_search_func(my_set, value)
        my_set_sorted = sorted(my_set)

        if order == len(my_set):
            min_val = -1
        else:
            min_val = my_set_sorted[order]
            
        
        print(min_val)