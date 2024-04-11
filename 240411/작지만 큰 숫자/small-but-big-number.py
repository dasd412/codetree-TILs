from sortedcontainers import SortedSet

ss=SortedSet()

n,m = list(map(int, input().split()))
arr = list(map(int, input().split()))
query = list(map(int, input().split()))

# 계산의 편의를 위해 음수화
for elem in arr:
    ss.add(-elem)

for x in query:
    index=ss.bisect_left(-x)

    if index<len(ss):
        print(-ss[index])
        ss.remove(ss[index])
    else:
        print(-1)