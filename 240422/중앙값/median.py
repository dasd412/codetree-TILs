import heapq

t=int(input())

for i in range(t):
    m=int(input())
    arr = list(map(int, input().split()))

    median=arr[0]

    # 중앙값보다 작은 값을 관리하는 힙.
    max_heap=[]

    # 중앙값보다 큰 값을 관리하는 힙.
    min_heap=[]
    print(median,end=' ')
    for i in range(1,len(arr)):
        # 짝수 번째 원소를 읽는 경우
        if i%2==1:
            if arr[i]<median:
                heapq.heappush(max_heap,-arr[i])
            else:
                heapq.heappush(min_heap,arr[i])
        # 홀수 번째 원소를 읽는 경우
        else:
            if len(min_heap)<len(max_heap):
                candidate=-heapq.heappop(max_heap)
            else:
                candidate=heapq.heappop(min_heap)
            
            temp=[candidate,arr[i],median]

            temp.sort()

            heapq.heappush(max_heap,-temp[0])
            median=temp[1]
            heapq.heappush(min_heap,temp[2])
            print(median,end=' ')
    print()