from sortedcontainers import SortedSet

ss=SortedSet()

n,m = list(map(int, input().split()))
arr = list(map(int, input().split()))

for elem in arr:
    ss.add(elem)

for i in range(m):
    x=int(input())
    
    index=ss.bisect_left(x)
    if index==len(arr):
        print(-1)
    else:
        print(ss[index])