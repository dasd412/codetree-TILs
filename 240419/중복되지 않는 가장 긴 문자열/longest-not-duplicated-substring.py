string=input()

answer=0

left=0
right=0

str_set=set()

while right<len(string):
    if string[right] not in str_set:
        str_set.add(string[right])
        answer=max(answer,len(str_set))
        right+=1
    else:
        str_set.remove(string[left])
        left+=1

print(answer)