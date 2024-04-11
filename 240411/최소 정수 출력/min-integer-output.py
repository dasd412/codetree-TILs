import heapq

heap=[]

n=int(input())

for i in range(n):
    x=int(input())
    if x==0:
        if heap:
            popped=heapq.heappop(heap)
            print(popped)
        else:
            print(0)
    else:
        heapq.heappush(heap,x)