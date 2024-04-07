import math
from sortedcontainers import SortedDict

n=int(input())

sd=SortedDict()

for i in range(n):
    s=input()
    if s not in sd:
        sd[s]=0
    sd[s]+=1

for key,value in sd.items():
    ratio=(value/n)*100
    formatted_percentage = "{:.4f}".format(ratio)
    print(key+' '+formatted_percentage)