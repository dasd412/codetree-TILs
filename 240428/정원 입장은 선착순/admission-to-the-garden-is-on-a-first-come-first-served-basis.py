import heapq

n=int(input())

# (a,i,t) 순. 시작 시간이 가장 빠른 순서대로 넣는다. 만약 시작 시간이 같을 경우엔 번호순이 작은 순서다.
times=[]

for i in range(n):
    a,t=list(map(int, input().split()))
    heapq.heappush(times,(a,i,t))


answer=0

# 대기하고 있는 사람 우선 순위 큐. 번호표 순 (a,i,t)-> (i,a,t)
wait_queue=[]

start,number,wait=heapq.heappop(times)

current_time=start+wait

while len(times) or len(wait_queue):
    
    while len(times):
        if times[0][0]<=current_time:
            start,number,wait=heapq.heappop(times)
            heapq.heappush(wait_queue,(number,start,wait))
        else:
            break
    
    if len(wait_queue):
        i,a,t=heapq.heappop(wait_queue)
        answer=max(answer,current_time-a)
        current_time+=t
    else:
        a,i,t=heapq.heappop(times)
        current_time=a+t

print(answer)