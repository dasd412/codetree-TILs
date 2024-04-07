from sortedcontainers import SortedDict

sd=SortedDict()

n = int(input())

for i in range(n):
    s=input()
    if s not in sd:
        sd[s]=0
    sd[s]+=1

for key,value in sd.items():
    print(key+' '+str(value))