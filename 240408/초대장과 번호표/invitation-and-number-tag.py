n,g = list(map(int, input().split()))

arr=[]

for i in range(g):
    li= list(map(int, input().split()))
    arr.append(li[1:])

arr.sort(key=lambda x : len(x))

person={1}

for li in arr:

    temp=set()
    for i in range(len(li)):
        temp.add(li[i])

    # 딱 한 사람만 못 받았을 경우 집합을 합한다.
    if len(temp-person)==1:
        person=person|temp

# # 1로 시작하지 않는 경우도 포함하기 위해 한 번 더 해야함.
for li in arr:

    temp=set()
    for i in range(len(li)):
        temp.add(li[i])

    if len(temp-person)==1:
        person=person|temp

print(len(person))