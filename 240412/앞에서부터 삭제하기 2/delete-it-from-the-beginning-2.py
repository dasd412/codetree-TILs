import heapq
import sys

n=int(input())
arr=list(map(int,input().split()))

# (정수 값, 인덱스)
heap=[]

for i,elem in enumerate(arr):
    heapq.heappush(heap,(elem,i))

answer=-sys.maxsize

sums=sum(arr)

for i in range(n-2):
    sums-=arr[i]

    avg=sums

    while heap:
        number,index=heap[0]

        # 아직 남아 있는 정수라면,
        if index>i:
            avg-=number
            break
        # 이미 지나간 것이면 제거해야한다.
        else:
            heapq.heappop(heap)

    answer=max(answer,avg/(n-i-2))

print("{:.2f}".format(answer))