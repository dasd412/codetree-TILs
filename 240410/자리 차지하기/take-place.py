from sortedcontainers import SortedSet

ss=SortedSet()

n,m = list(map(int, input().split()))
arr = list(map(int, input().split()))

for i in range(1,m+1):
    ss.add(i)

answer=0

# 최대한 많이 앉힐려면, 앞자리부터 최대한 번호가 높은 것을 택해야 한다.
# 시간 복잡도는 O(N log M)
for elem in arr:
    if len(ss)==0:
        break
    index=ss.bisect_right(elem)-1
    if ss[index]<=elem:
        answer+=1
        ss.remove(ss[index])

print(answer)