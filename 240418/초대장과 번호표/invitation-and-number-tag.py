from collections import deque

n,g=list(map(int,input().split()))

arr=[set() for i in range(g)]

for i in range(g):
    group=list(map(int,input().split()))[1:]
    for person in group:
        arr[i].add(person)

queue=deque()
queue.append(1)

answer=0

while queue:
    number=queue.popleft()
    answer+=1

    for elem in arr:
        if number in elem:
            elem.remove(number)
        if len(elem)==1:
            queue.append(list(elem)[0])

print(answer)