n,k = list(map(int, input().split()))

arr = list(map(int, input().split()))

# 조합으로 할 경우 n이 10만이므로 너무 크다.
# x+y=k를 활용한다. 즉 x가 이미 있으면 k-y를 이용한다.

number_dict=dict()

answer=0

for elem in arr:
    if elem not in number_dict:
        number_dict[elem]=0
    
    if k-elem in number_dict:
        answer+=number_dict[k-elem]

    number_dict[elem]+=1
    
print(answer)