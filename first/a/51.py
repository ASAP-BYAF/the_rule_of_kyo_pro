from collections import deque

# LIFOキュー(スタック)を作成
stack = deque()

q = int(input())

for _ in range(q):
    num, *title = input().split()

    if num == '1':
        stack.append(title[0])
    elif num == '2':
        print(stack[-1])
    elif num == '3':
        stack.pop()