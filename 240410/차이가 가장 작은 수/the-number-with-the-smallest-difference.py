from sortedcontainers import SortedSet
import sys

ss=SortedSet()

n,m=list(map(int, input().split()))

for i in range(n):
    num=int(input())
    ss.add(num)

# sorted_set은 오름차순으로 정렬되있음을 이용한다.
# left ~ right 투포인터를 활용.

left=0
right=len(ss)-1

answer=sys.maxsize

while left<=right:
    if abs(ss[left]-ss[right])>=m:
        answer=min(answer,abs(ss[left]-ss[right]))

    if left+1<right and abs(ss[left+1]-ss[right])>=m:
        left+=1
    elif right-1>left and abs(ss[left]-ss[right-1])>=m:
        right-=1
    else:
        break


if answer==sys.maxsize:
    print(-1)
else:
    print(answer)