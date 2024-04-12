import heapq

t=int(input())

for i in range(t):
    # 중앙값보다 크거나 같은 값중 최솟값을 관리한다.
    min_heap=[]

    # 중앙값보다 작은 값 중 최댓값을 관리한다.
    max_heap=[]

    m=int(input())
    arr=list(map(int,input().split()))

    median=arr[0]
    print(median,end=' ')
    for j in range(1,len(arr)):
        # 짝수 번째인 경우 중앙값이 상관없으므로 현재 중앙값을 기준으로 하여 힙에 넣는다.
        if j%2==1:
            if median<arr[j]:
                heapq.heappush(min_heap,arr[j])
            else:
                heapq.heappush(max_heap,-arr[j])
        # 홀수 번째인 경우, min_heap과 max_heap의 크기가 맞지 않는다. 
        # 왜냐하면 중앙값 median은 heap에 의해 관리되지 않으므로 홀수 번째인 경우 힙의 전체 개수는 홀수개이기 때문
        else:
            # 크기가 더 큰 쪽에서 중앙값 후보를 가져온다.
            if len(min_heap)>len(max_heap):
                popped=heapq.heappop(min_heap)
            else:
                popped=-heapq.heappop(max_heap)
            
            # 현재 중앙값, arr[i], 기존 힙의 후보를 정렬하여 새로운 중앙값을 선정한다.
            li=sorted([median,arr[j],popped])

            median=li[1]
            heapq.heappush(max_heap,-li[0])
            heapq.heappush(min_heap,li[2])
            print(median,end=' ')
    print()