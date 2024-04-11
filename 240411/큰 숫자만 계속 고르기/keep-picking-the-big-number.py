import heapq

n,m = list(map(int, input().split()))
arr = list(map(int, input().split()))

heap=[]

for elem in arr:
    heapq.heappush(heap,-elem)

for i in range(m):
    popped=-heapq.heappop(heap)
    popped-=1
    heapq.heappush(heap,-popped)

print(-heap[0])