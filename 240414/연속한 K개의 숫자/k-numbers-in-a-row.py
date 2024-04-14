import heapq
import sys

n,k,b= list(map(int, input().split()))

# 누적합의 경우 구간의 누적된 합을 빠르게 구할 때도 사용하지만
# 지금까지 나온 개수들을 누적할 때도 사용한다.
heap=[]

for i in range(b):
    x=int(input())
    heapq.heappush(heap,x)

prefix_sum=[0]*(n+1)

val=0
for i in range(1, n+1):
    if heap[0]==i:
        heapq.heappop(heap)
        val+=1
    prefix_sum[i]=val

answer=sys.maxsize
for i in range(k,n+1):
    answer=min(answer,prefix_sum[i]-prefix_sum[i-k])
print(answer)