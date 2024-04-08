from collections import deque

n,g = list(map(int, input().split()))

groups=[]

for i in range(g):
    li= list(map(int, input().split()))
    
    group=set()
    
    for i in range(len(li)):
        if i>0:
            group.add(li[i])
    
    groups.append(group)
        
queue=deque()
queue.append(1)

visited=[False]*(n+1)

# O(NG)
while queue:
    person=queue.popleft()
    visited[person]=True

    for group in groups:
        if person in group:
            group.remove(person)

            # 단 하나만 남게 될 경우
            if len(group)==1:
                queue.append(group.pop())

answer=0
for i in range(1,len(visited)):
    if visited[i]:
        answer+=1

print(answer)