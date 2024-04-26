import sys

n,k,b=list(map(int, input().split()))

arr=[i+1 for i in range(n)]

removed=set()

for i in range(b):
    num=int(input())
    removed.add(num)

answer=sys.maxsize    

for left in range(n):

    count=0

    right=left
    while right<n and right-left<k:
        if arr[right] in removed:
            count+=1
        right+=1

    answer=min(answer,count)

    if n-left<=k:
        break

print(answer)