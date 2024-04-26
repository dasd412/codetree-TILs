import sys

n,k,b=list(map(int, input().split()))

arr=[i+1 for i in range(n)]
removed=set()
for i in range(b):
    num=int(input())
    removed.add(num)

answer=sys.maxsize    

"""
투 포인터 풀이보단 누적합 풀이가 더 효율적이다.
"""

prefix_sum=[0]*(n+1)

for i in range(1,n+1):
    if arr[i-1] in removed:
        prefix_sum[i]+=1
    
for i in range(1,n+1):
    prefix_sum[i]+=prefix_sum[i-1]

for left in range(1,n+1):
    right=left+k-1
    if right>=n:
        break
    answer=min(answer,prefix_sum[right]-prefix_sum[left-1])

print(answer)