from collections import defaultdict

# d[x]=y
d=defaultdict(int)

n=int(input())
for i in range(n):
    x,y=list(map(int,input().split()))

    if x in d:
        if y<d[x]:
            d[x]=y
    else:
        d[x]=y

answer=0
for key,value in d.items():
    answer+=value

print(answer)