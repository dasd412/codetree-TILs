import sys

n,k = list(map(int, input().split()))
arr = list(map(int, input().split()))

answer=sys.maxsize

right=0
left=0

count=0

while right<n:
    if count<k:
        if arr[right]==1:
            count+=1
        right+=1
    else:
        if arr[left]==1:
            count-=1
        left+=1
    if count==k:
        answer=min(answer,right-left)

while left<n:
    if count==k:
        answer=min(answer,right-left)
        if arr[left]==1:
            count-=1
        left+=1
    else:
        break

if answer==sys.maxsize:
    print(-1)
else:
    print(answer)