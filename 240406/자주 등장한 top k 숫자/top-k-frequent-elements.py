from collections import defaultdict

n,k = list(map(int, input().split()))
arr = list(map(int, input().split()))

counts=defaultdict(int)

for elem in arr:
    counts[elem]+=1

li=[]

for key,value in counts.items(): 
    li.append((key,value))

li.sort(key=lambda x : (-x[1],-x[0]))

for i in range(k):
    print(li[i][0],end=' ')