from sortedcontainers import SortedSet

ss=SortedSet()

n,k = list(map(int, input().split()))
arr = list(map(int, input().split()))

for elem in arr:
    ss.add(elem)

for i in range(k):
    print(ss[-1-i],end=' ')