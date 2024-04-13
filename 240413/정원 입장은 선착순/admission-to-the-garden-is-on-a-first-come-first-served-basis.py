import heapq

n=int(input())

heap=[]

arr=[0]*n

for i in range(n):
    a,t=list(map(int,input().split()))
    # (도착 시간, 번호표, 머무르는 시간)
    heapq.heappush(heap,(a,i,t))

a,i,t=heapq.heappop(heap)
time=a+t

# 기다리고 있는 사람을 관리하는 우선순위 큐. 도착 시간이 아니라 번호 표를 기준으로 우선순위가 됨.
waited=[]

while heap or waited:

    # O(NlogN)
    while heap:
        # 현재 진행중인 시간보다 먼저 온 사람들 다 찾아 놓기
        if heap[0][0]<=time: 
            a,i,t=heapq.heappop(heap)
            # 번호 표를 우선순위로
            heapq.heappush(waited,(i,a,t))
        else:
            break

    # 기다리는 사람이 있으면, 기다리는 사람 먼저
    if waited:
        i,a,t=heapq.heappop(waited)
        # 기다릴 필요가 없는 경우
        if a>=time:
            time=a

        arr[i]=time-a
        time+=t

    # 기다리는 사람 없으면, 다음 사람 넣기
    else:
        a,i,t=heapq.heappop(heap)
        heapq.heappush(waited,(i,a,t))

# O(N)
print(max(arr))