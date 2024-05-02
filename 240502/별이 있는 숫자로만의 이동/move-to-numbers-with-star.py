n,k=list(map(int,input().split()))

arr=[[0]*n for _ in range(n)]

for i in range(n):
    split=list(map(int,input().split()))
    for j in range(n):
        arr[i][j]=split[j]

dp=[[0]*(n+1) for _ in range(n+1)]

# 행 단위로 누적합을 구한다.
for i in range(1,n+1):
    for j in range(1,n+1):
        dp[i][j]=dp[i][j-1]+arr[i-1][j-1]

answer=0

for i in range(1,n+1):
    for j in range(1,n+1):
        sums=0

        for row in range(i-k,i+k+1):
            # row 행에서의 열 범위를 구한다.
            col_range=k-abs(i-row)

            # 유효한 row 행일 경우에만 계산한다.
            if 1<=row<=n:
                # 열의 범위 역시 1<=c<=n임을 유의해야 한다.
                sums+=dp[row][min(j+col_range,n)]-dp[row][max(j-col_range-1,0)]
        answer=max(answer,sums)

print(answer)