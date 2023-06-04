import heapq

heapque = []

q = int(input())

for _ in range(q):
    num, *value = input().split()

    if num == '1':
        heapq.heappush(heapque, int(value[0]))
    elif num == '2':
        min = heapq.heappop(heapque)
        print(min)
        heapq.heappush(heapque,min)
    elif num == '3':
        heapq.heappop(heapque)