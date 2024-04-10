import sys
from sortedcontainers import SortedSet


n,m=list(map(int, input().split()))

ss=SortedSet()
for i in range(n):
    num=int(input())
    ss.add(num)

answer=sys.maxsize

for i in range(n):
    # 차이가 m 이상 나는 것 중 가장 첫 번째로 만나는 것을 택한다. 
    index=ss.bisect_right(ss[-1-i]-m)-1

    if ss[-1-i]-ss[index]>=m:
        answer=min(answer,ss[-1-i]-ss[index])
        if ss[-1-i]-ss[index]==m:
            break


if answer==sys.maxsize:
    print(-1)
else:
    print(answer)