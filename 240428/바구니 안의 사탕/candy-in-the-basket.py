from collections import defaultdict

n,k= list(map(int, input().split()))

candy_dict=defaultdict(int)

# O(10만)
for i in range(n):
    count,position= list(map(int, input().split()))
    candy_dict[position]+=count

arr=[]

# O(10만)
for key,value in candy_dict.items():
    arr.append((key,value))

# 위치 순으로 정렬
arr.sort()

# 초기 값 찾기 O(10만)
answer=0
for i in range(len(arr)):
    if 0<=arr[i][0]<=2*k:
        answer+=arr[i][1]
    else:
        break

count=answer
left=0
right=2*k
# O(1,000,000)=O(10^6)
for c in range(k+1,1000001):
    if left in candy_dict:
        count-=candy_dict[left]
    left+=1
    right+=1

    if right in candy_dict:
        count+=candy_dict[right]

    answer=max(answer,count)

print(answer)