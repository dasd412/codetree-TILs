from collections import defaultdict

s,k=list(input().split())
k=int(k)

left=0
right=0

answer=0

ch_dict=defaultdict(int)

def get_sum(target):
    temp=set()
    temp.add(target)
    for key,value in ch_dict.items():
        if value>0:
            temp.add(key)

    return len(temp)

while right<len(s):
    if get_sum(s[right])<=k:
        ch_dict[s[right]]+=1

        temp=0
        for key,value in ch_dict.items():
            temp+=value

        answer=max(answer,temp)

        right+=1
    else:
        ch_dict[s[left]]-=1
        left+=1
    
print(answer)