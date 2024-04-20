from sortedcontainers import SortedSet

ss=SortedSet()
n,m = list(map(int, input().split()))
arr = list(map(int, input().split()))

for i in range(m):
    ss.add(i+1)

for elem in arr:
    ss.remove(elem)
    print(ss[-1])