from collections import defaultdict

s,k=list(input().split())

k=int(k)

ch_dict=defaultdict(int)

left=0
right=0

answer=0

def get_type_count():
    count=0
    for key,value in ch_dict.items():
        if value>0:
            count+=1
    return count
while right<len(s):
    
    if get_type_count()<=k:
        ch_dict[s[right]]+=1
        right+=1
    else:
        ch_dict[s[left]]-=1
        left+=1
    
    if get_type_count()==k:
        answer=max(answer,right-left)

print(answer)