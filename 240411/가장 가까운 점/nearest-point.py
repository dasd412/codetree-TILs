import heapq

heap=[]

n,m=list(map(int, input().split()))

for i in range(n):
    x,y=list(map(int, input().split()))

    heapq.heappush(heap,(abs(x)+abs(y),x,y))

for i in range(m):
    distance,x,y=heapq.heappop(heap)
    heapq.heappush(heap,(abs(x+2)+abs(y+2),x+2,y+2))

distance,x,y=heapq.heappop(heap)
print(x,y)