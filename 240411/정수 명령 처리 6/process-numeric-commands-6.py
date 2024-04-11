import heapq

n=int(input())

max_heap=[]

for i in range(n):
    split=list(input().split())
    if split[0]=='push':
        heapq.heappush(max_heap,-int(split[1]))
    elif split[0]=='pop':
        popped=heapq.heappop(max_heap)
        print(-popped)
    elif split[0]=='size':
        print(len(max_heap))
    elif split[0]=='empty':
        if len(max_heap):
            print(0)
        else:
            print(1)
    elif split[0]=='top':
        print(-max_heap[0])