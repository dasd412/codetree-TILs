n,q = list(map(int, input().split()))

area=[0]* 1000002

arr = list(map(int, input().split()))
for elem in arr:
    area[elem+1]=1

for i in range(1,len(area)):
    area[i]+=area[i-1]

for _ in range(q):
    a,b = list(map(int, input().split()))
    print(area[b+1]-area[a])