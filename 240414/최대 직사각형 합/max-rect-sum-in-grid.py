import sys

n=int(input())

arr=[[0]*n for _ in range(n)]

for i in range(n):
    split=list(map(int,input().split()))
    for j in range(n):
        arr[i][j]=split[j]

dp=[[0]*(n+1) for _ in range(n+1)]

# O(n^2)=O(90000)
for i in range(1,n+1):
    for j in range(1,n+1):
        dp[i][j]=dp[i][j-1]+dp[i-1][j]-dp[i-1][j-1]+arr[i-1][j-1]

answer=-sys.maxsize

# (i,j)를 좌표, k를 길이라고 한다.
# O(N^3)=O(300^3) ~ O(10^6)이므로 충분할 듯.
for i in range(1,n+1):
    for j in range(1,n+1):
        for k in range(1,max(i,j)+1):
            # 정사각형
            cand1=dp[i][j]-dp[i][j-k]-dp[i-k][j]+dp[i-k][j-k] if i-k>=0 and j-k>=0 else -sys.maxsize

            # 세로
            cand2=dp[i][j]-dp[i-k][j]-dp[i][j-1]+dp[i-k][j-1] if i-k>=0 and j-1>=0 else -sys.maxsize

            # 가로
            cand3=dp[i][j]-dp[i][j-k]-dp[i-1][j]+dp[i-1][j-k] if j-k>=0 and i-1>=0 else -sys.maxsize

            answer=max(answer,cand1,cand2,cand3)
            
print(answer)