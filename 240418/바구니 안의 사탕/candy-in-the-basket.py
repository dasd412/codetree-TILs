n,k=list(map(int,input().split()))

# position[좌표]=사탕의 개수
position=[0]*1000001

# dp[인덱스]=position의 인덱스-1까지의 누적 개수
#[c-K,c+K] 구간은 dp[c+K]-dp[c-K-1]로 O(1)에 빠르게 구할 수 있다.
dp=[0]*1000002

# 제일 마지막에 놓인 사탕의 위치
max_pos=0

# O(n)
for i in range(n):
    count,pos=list(map(int,input().split()))
    position[pos]+=count
    max_pos=max(max_pos,pos)
    dp[pos+1]=position[pos]

# O(n)
for i in range(1,len(dp)):
    dp[i]+=dp[i-1]

answer=0

# c = dp의 인덱스 => positon의 인덱스 -1
# O(n)
for c in range(len(dp)):
    if 1<=c-k and c+k<len(dp):
        val=dp[c+k]-dp[c-k-1]
        answer=max(answer,val)

# O(3n)
print(answer)