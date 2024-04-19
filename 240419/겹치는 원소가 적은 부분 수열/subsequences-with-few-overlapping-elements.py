from collections import defaultdict




n,k = list(map(int, input().split()))
arr = list(map(int, input().split()))

counter=defaultdict(int)

left=0
right=0
answer=0

def is_ok(number:int)->bool:
    if counter[number]+1<=k:
        return True
    else:
        return False


while right<n:

    # 오른쪽 원소를 집어넣어도 괜찮다면, 실제로 집어 넣는다.
    if is_ok(arr[right]):
        answer=max(answer,right-left+1)
        counter[arr[right]]+=1
        right+=1
    # 집어 넣을 수 없다면, 왼쪽 범위를 줄인다.
    else:
        counter[arr[left]]-=1
        left+=1
    
print(answer)