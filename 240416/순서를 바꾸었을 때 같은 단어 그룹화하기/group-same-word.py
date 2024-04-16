from collections import defaultdict

d=defaultdict(int)

n=int(input())

for _ in range(n):
    s=input()
    s=sorted(s)

    string=''
    for ch in s:
        string+=ch
        
    d[string]+=1

answer=0
for key,value in d.items():
    answer=max(answer,value)
print(answer)