my_dict = {}

q = int(input())

for _ in range(q):
    num, student, *score = input().split()

    if score:
        my_dict[student] = int(score[0])
    else:
        print(my_dict[student])
