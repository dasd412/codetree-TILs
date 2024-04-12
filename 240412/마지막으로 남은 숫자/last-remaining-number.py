import heapq

n=int(input())

arr=list(map(int,input().split()))

heap=[]

for elem in arr:
    heapq.heappush(heap,-elem)

while len(heap)>=2:
    pop1=-heapq.heappop(heap)
    pop2=-heapq.heappop(heap)

    if pop1!=pop2:
        heapq.heappush(heap,-(pop1-pop2))

if len(heap)==1:
    print(-heap[0])
else:
    print(-1)