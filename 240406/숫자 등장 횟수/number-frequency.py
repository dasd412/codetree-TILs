from collections import defaultdict

n,m=list(map(int, input().split()))
arr=list(map(int, input().split()))
query=list(map(int, input().split()))

count=defaultdict(int)
for elem in arr:
    count[elem]+=1

for q in query:
    print(count[q],end=' ')