from collections import defaultdict

n,k = list(map(int, input().split()))
arr = list(map(int, input().split()))

# x+y+z=k => x+y=k-z를 활용한다.
#xy_dict[x+y]=(x,y)
xy_dict=defaultdict(list)

# 시간 복잡도 = 10^6
for i in range(n):
    for j in range(i+1,n):
        xy_dict[arr[i]+arr[j]].append((i,j))

answer=set()

# 시간 복잡도 = 10^6
for i in range(n):
    for x,y in xy_dict[k-arr[i]]:
        if i!=x and i!=y:
            tup=[i,x,y]
            tup.sort()
            answer.add(tuple(tup))

print(len(answer))