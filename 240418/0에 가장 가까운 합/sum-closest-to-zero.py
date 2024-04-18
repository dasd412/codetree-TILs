import sys

n=int(input())
arr = list(map(int, input().split()))

# 두 수의 합이 0에 가깝게하기 위해 정렬한다.
arr.sort()

left=0
right=len(arr)-1

answer=sys.maxsize

while left<right:
    # 양쪽 끝을 더했더니 양수라면, 오른쪽 범위를 줄여보자. (양수 값이 줄어드는 효과)
    if arr[left]+arr[right]>0:
        answer=min(answer,abs(arr[left]+arr[right]))
        right-=1
    elif arr[left]+arr[right]==0:
        answer=0
        break
    # 양쪽 끝을 더했더니 음수라면, 왼쪽 범위를 줄여보자. (음수 값이 줄어드는 효과)
    else:
        answer=min(answer,abs(arr[left]+arr[right]))
        left+=1
print(answer)