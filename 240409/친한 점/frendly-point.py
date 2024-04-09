from sortedcontainers import SortedSet

ss=SortedSet()

n,m = list(map(int, input().split()))

for i in range(n):
    x,y = list(map(int, input().split()))
    ss.add((x,y))

for i in range(m):
    qx,qy = list(map(int, input().split()))
    index=ss.bisect_left((qx,qy))

    if index==len(ss):
        print('-1 -1')
    else:
        print(str(ss[index][0])+' '+str(ss[index][1]))