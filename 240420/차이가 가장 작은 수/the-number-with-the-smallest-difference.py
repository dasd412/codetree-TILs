# 투포인터 풀이. 시간 복잡도는 O(Nlog N + N)
import sys
n,m=list(map(int,input().split()))

arr=[]

for i in range(n):
    num=int(input())
    arr.append(num)

arr.sort()

answer=sys.maxsize

right=1
for left in range(n):
    while right<n:
        if arr[right]-arr[left]<m:
            right+=1
        else:
            break
    if right<n:
        answer=min(answer,arr[right]-arr[left])

print(answer)