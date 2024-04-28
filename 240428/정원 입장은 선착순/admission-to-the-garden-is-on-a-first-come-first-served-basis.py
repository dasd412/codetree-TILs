import heapq

n=int(input())

times=[]

for i in range(n):
    a,t=list(map(int, input().split()))
    heapq.heappush(times,(a,t,i))


answer=0

# 대기하고 있는 사람 우선 순위 큐. 번호표 순 (a,t,i)-> (i,a,t)
wait_queue=[]

start,wait,number=heapq.heappop(times)

current_time=start+wait

while len(times) or len(wait_queue):
    
    while len(times):
        if times[0][0]<=current_time:
            start,wait,number=heapq.heappop(times)
            heapq.heappush(wait_queue,(number,start,wait))
        else:
            break
    
    if len(wait_queue):
        i,a,t=heapq.heappop(wait_queue)
        answer=max(answer,current_time-a)
        current_time+=t
    else:
        a,t,i=heapq.heappop(times)
        current_time=a+t

print(answer)