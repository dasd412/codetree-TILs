from collections import deque

n,g=list(map(int,input().split()))

arr=[set() for i in range(g)]

for i in range(g):
    group=list(map(int,input().split()))[1:]
    for person in group:
        arr[i].add(person)

queue=deque()
queue.append(1)

answer=set()

while queue:
    number=queue.popleft()
    answer.add(number)

    for elem in arr:
        if number in elem:
            elem.remove(number)
            if len(elem)==1:
                queue.append(elem.pop())

print(len(answer))