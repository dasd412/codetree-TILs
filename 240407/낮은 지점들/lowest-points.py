from collections import defaultdict

n = int(input())

# dims[x]=y
dims=defaultdict(int)

for i in range(n):
    x,y = list(map(int, input().split()))
    if x in dims:
        dims[x]=min(dims[x],y)
    else:
        dims[x]=y

answer=0
for key, value in dims.items():
    answer+=value

print(answer)