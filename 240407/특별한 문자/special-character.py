s=input()

# counter[문자]=개수,인덱스
counter=dict()

for i in range(len(s)):
    if s[i] not in counter:
        counter[s[i]]=[1,i]
    else:
        counter[s[i]][0]+=1


arr=[]

for k,v in counter.items():
    if v[0]==1:
        arr.append((k,v[1]))

if len(arr):
    arr.sort(key=lambda x :x[1])
    print(arr[0][0])
else:
    print("None")