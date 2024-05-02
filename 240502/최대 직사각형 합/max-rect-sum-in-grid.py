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

def get_sum(x1:int,y:int,x2:int)->int:
    return dp[x2][y]-dp[x1-1][y]-dp[x2][y-1]+dp[x1-1][y-1]

# x1 행 ~ x2 행에서 존재하는 직사각형들 중 가장 큰 합을 찾아내는 함수
def get_area(x1:int,x2:int)->int:

    # x1~x2 행일 때, y열까지 계산했을 경우 합의 최댓값을 기록한 자료구조
    columns=[0]*(n+1)

    for y in range(1,n+1):
        column_sum=get_sum(x1,y,x2)
        columns[y]=max(column_sum,columns[y-1]+column_sum)

    max_area=-sys.maxsize

    # 음수가 존재하기 때문에 열이 늘어난다고 해서 최댓값을 보장하지 않는다. 따라서 처음부터 확인해봐야 한다.
    for y in range(1,n+1):
        max_area=max(max_area,columns[y])
    return max_area

answer=-sys.maxsize

for x1 in range(1,n+1):
    for x2 in range(x1,n+1):
        area=get_area(x1,x2)
        answer=max(answer,area)

print(answer)