n,g = list(map(int, input().split()))

arr=[]

person=set()

for i in range(g):
    li= list(map(int, input().split()))
    if li[0]==2 and 1 in li[1:]:
        person.add(li[1])
        person.add(li[2])

    arr.append(li[1:])

# O(GN)
for li in arr:

    temp=set()
    for i in range(len(li)):
        temp.add(li[i])

    # 딱 한 사람만 못 받았을 경우 집합을 합한다.
    if len(temp-person)==1:
        person=person|temp

for li in arr:

    temp=set()
    for i in range(len(li)):
        temp.add(li[i])

    if len(temp-person)==1:
        person=person|temp

print(len(person))