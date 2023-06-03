import queue

# LIFOキュー(スタック)を作成
stack = queue.LifoQueue()

q = int(input())

for _ in range(q):
    num, *title = input().split()

    if num == '1':
        stack.put(title[0])
    elif num == '2':
        top = stack.get()
        print(top)
        stack.put(top)
    elif num == '3':
        stack.get()