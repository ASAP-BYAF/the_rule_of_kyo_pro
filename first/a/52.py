from collections import deque

stack = deque()

q = int(input())

for _ in range(q):
    num, *title = input().split()

    if num == '1':
        stack.append(title[0])
    elif num == '2':
        print(stack[0])
    elif num == '3':
        stack.popleft()