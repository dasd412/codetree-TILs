from collections import defaultdict

n = int(input())

counts=defaultdict(int)

for i in range(n):
    s=input()
    counts[s]+=1

answer=0

for key,value in counts.items():
    answer=max(answer,value)

print(answer)