import sys

n,k=list(map(int,input().split()))
arr=list(map(int,input().split()))

prefix_sum=[0]*(n+1)

val=0
for i in range(1,n+1):
    val+=arr[i-1]
    prefix_sum[i]=val

answer=-sys.maxsize

for i in range(1,n+2-k):
    answer=max(answer,prefix_sum[i+k-1]-prefix_sum[i-1])
print(answer)