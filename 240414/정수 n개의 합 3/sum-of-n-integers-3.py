n,k = list(map(int, input().split()))

arr=[[0]*n for _ in range(n)]

for i in range(n):
    split = list(map(int, input().split()))
    for j in range(n):
        arr[i][j]=split[j]

prefix_sum=[[0]*(n+1) for _ in range(n+1)]

for i in range(1,n+1):
    for j in range(1,n+1):
        prefix_sum[i][j]=prefix_sum[i-1][j]+prefix_sum[i][j-1]-prefix_sum[i-1][j-1]+arr[i-1][j-1]

answer=0

for i in range(k,n+1):
    for j in range(k,n+1):
        val=prefix_sum[i][j]-prefix_sum[i-k][j]-prefix_sum[i][j-k]+prefix_sum[i-k][j-k]
        answer=max(answer,val)

print(answer)