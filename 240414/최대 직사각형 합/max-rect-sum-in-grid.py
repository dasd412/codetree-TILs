import sys

n=int(input())

arr=[[0]*n for _ in range(n)]

for i in range(n):
    split=list(map(int,input().split()))
    for j in range(n):
        arr[i][j]=split[j]

prefix_sum=[[0]*(n+1) for _ in range(n+1)]

# O(n^2)=O(90000)
for i in range(1,n+1):
    for j in range(1,n+1):
        prefix_sum[i][j]=prefix_sum[i][j-1]+prefix_sum[i-1][j]-prefix_sum[i-1][j-1]+arr[i-1][j-1]

answer=-sys.maxsize

# (i,j)를 직사각형 범위라 한다.
# O(n^4)이므로 시간초과일듯?
for i in range(1,n+1):
    for j in range(1,n+1):
        for k in range(i,n+1):
            for l in range(j,n+1):
                val=prefix_sum[k][l]-prefix_sum[k-i][l]-prefix_sum[k][l-j]+prefix_sum[k-i][l-j]
                answer=max(answer,val)

print(answer)