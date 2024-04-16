from collections import defaultdict

n,k = list(map(int, input().split()))
arr = list(map(int, input().split()))

"""
단순히 계산하면 x+y+z=k이므로 O(N^3)=O(10^9)이므로 시간초과다.

아무리 느려도 O(N^2 NlogN)풀이가 필요하다.

x+y=k-z를 활용한다.

x+y로 만들 수 있는 쌍은 N^2개이다.
"""

# (x+y,x인덱스,y인덱스)
xy=defaultdict(list)

# O(N^2)
for i in range(n):
    for j in range(i+1,n):
        x=arr[i]
        y=arr[j]
        xy[x+y].append((i,j))

answer=set()

# O(N^2)
for i in range(n):
    z=arr[i]
    if k-z in xy:
        for a,b in xy[k-z]:
            if i!=a and i!=b:
                tup=tuple(sorted([i,a,b]))
                answer.add(tup) 

# 총 시간 복잡도는 O(N^2)+O(N^2)
print(len(answer))