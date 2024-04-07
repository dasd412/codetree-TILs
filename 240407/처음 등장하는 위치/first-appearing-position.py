from sortedcontainers import SortedDict

sd=SortedDict()

n=int(input())

arr = list(map(int, input().split()))

for i,elem in enumerate(arr):
    if elem not in sd:
        sd[elem]=i+1

for key,value in sd.items():
    print(str(key)+' '+str(value))