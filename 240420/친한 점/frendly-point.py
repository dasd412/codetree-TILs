from sortedcontainers import SortedSet

ss=SortedSet()

n,m= list(map(int, input().split()))

for i in range(n):
    x,y= list(map(int, input().split()))
    ss.add((x,y))

for i in range(m):
    x,y= list(map(int, input().split()))
    index=ss.bisect_left((x,y))
    if index<len(ss):
        print(str(ss[index][0])+' '+str(ss[index][1]))
    else:
        print("-1 -1")