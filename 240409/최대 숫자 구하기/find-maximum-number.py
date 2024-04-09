from sortedcontainers import SortedSet

ss=SortedSet()

n,m=list(map(int, input().split()))
arr=list(map(int, input().split()))

for i in range(1,m+1):
    ss.add(i)

for elem in arr:
    ss.remove(elem)
    print(ss[-1])