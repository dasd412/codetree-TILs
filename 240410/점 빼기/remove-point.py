from sortedcontainers import SortedSet

ss=SortedSet()

n,m = list(map(int, input().split()))
for i in range(n):
    x,y = list(map(int, input().split()))
    ss.add((x,y))

for i in range(m):
    k=int(input())
    # x좌표는 k보다 크거나 같고, y는 0보다 크거나 같은 것
    index=ss.bisect_left((k,0))

    if index<len(ss):
        print(str(ss[index][0])+' '+str(ss[index][1]))
        ss.remove(ss[index])
    else:
        print('-1 -1')