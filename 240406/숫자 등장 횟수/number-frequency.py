import sys
from collections import defaultdict

n,m=list(map(int,sys.stdin.readline().split(' ')))
arr=list(map(int,sys.stdin.readline().split(' ')))
query=list(map(int,sys.stdin.readline().split(' ')))

count=defaultdict(int)
for elem in arr:
    count[elem]+=1

for q in query:
    print(count[q],end=' ')