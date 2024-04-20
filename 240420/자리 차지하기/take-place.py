from sortedcontainers import SortedSet

n,m = list(map(int, input().split()))
arr = list(map(int, input().split()))

ss=SortedSet()
for i in range(m):
    ss.add(i+1)

answer=0

for elem in arr:
    index=ss.bisect_right(elem)-1
    if index<len(ss) and ss[index]<=elem:
        ss.remove(ss[index])
        answer+=1

print(answer)