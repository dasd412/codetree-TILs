import sys
from collections import defaultdict

n,d=list(map(int,input().split()))

arr=[]

for i in range(n):
    x,y=list(map(int,input().split()))
    arr.append((x,y))

# y 좌표 기준으로 오름차순 정렬
arr.sort(key=lambda x:x[1])

left=0
right=len(arr)-1

answer=sys.maxsize

# B-A는 구간인데, y좌표 기준으로 오름차순 정렬해서 y기준으로 범위를 좁혀보자. 그 때, x는 대소 비교를 할 필요 없다. 절댓값 씌우면 되지 않을까
while left<right:
    if arr[left][1]+arr[right][1]>=d:
        answer=min(answer,abs(arr[right][0]-arr[left][0]))
        right-=1
    else:
        left+=1

print(answer)