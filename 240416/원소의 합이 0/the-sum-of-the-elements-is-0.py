from collections import defaultdict

n=int(input())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
c=list(map(int,input().split()))
d=list(map(int,input().split()))

ab=defaultdict(int)
cd=defaultdict(int)

# O(N^2)
for i in range(n):
    for j in range(n):
        ab[a[i]+b[j]]+=1

# O(N^2)
for i in range(n):
    for j in range(n):
        cd[c[i]+d[j]]+=1

answer=0

for key,value in ab.items():
    if -key in cd:
        answer+=(value*cd[-key])
            
# O(3N^2)
print(answer)