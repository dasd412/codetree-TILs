import heapq

n=int(input())
arr=list(map(int,input().split()))

heap=[]

# O(nlogn)
for elem in arr:
    heapq.heappush(heap,elem)

    if len(heap)>=3:
        p1=heapq.heappop(heap)
        p2=heapq.heappop(heap)
        p3=heapq.heappop(heap)

        print(p1*p2*p3)

        heapq.heappush(heap,p1)
        heapq.heappush(heap,p2)
        heapq.heappush(heap,p3)
        
    else:
        print(-1)