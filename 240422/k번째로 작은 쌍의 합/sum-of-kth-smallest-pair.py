import heapq

n,m,k = list(map(int, input().split()))
a = list(map(int, input().split()))
b = list(map(int, input().split()))

a.sort()
b.sort()

# (a원소, b원소, b 인덱스)
heap=[]

# O(N)
for i in range(n):
    heapq.heappush(heap,(a[i]+b[0],a[i],b[0],0))

# O(K) * O(log min(M,N))
for i in range(k):
    sums,x,y,b_idx=heapq.heappop(heap)
    if b_idx+1<len(b):
        heapq.heappush(heap,(x+b[b_idx+1],x,b[b_idx+1],b_idx+1))
    if i==k-1:
        print(sums)