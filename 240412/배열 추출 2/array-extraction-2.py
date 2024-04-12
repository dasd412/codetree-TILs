import heapq

n=int(input())
heap=[]

for i in range(n):
    x=int(input())
    if x==0:
        if heap:
            popped=heapq.heappop(heap)
            print(popped[1])
        else:
            print(0)
    else:
        heapq.heappush(heap,(abs(x),x))