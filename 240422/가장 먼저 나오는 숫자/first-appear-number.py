n,m = list(map(int, input().split()))
arr = list(map(int, input().split()))
query = list(map(int, input().split()))

def lower_bound(x):
    left=0
    right=n-1
    min_idx=n

    while left<=right:
        mid=(left+right)//2

        if arr[mid]>=x:
            min_idx=min(min_idx,mid)
            right=mid-1
        else:
            left=mid+1
    
    return min_idx+1


def upper_bound(x):
    left=0
    right=n-1
    min_idx=n

    while left<=right:
        mid=(left+right)//2
        if arr[mid]>x:
            min_idx=min(min_idx,mid)
            right=mid-1
        else:
            left=mid+1

    return min_idx+1


for number in query:
    lower_idx=lower_bound(number)
    upper_idx=upper_bound(number)
    # # 상한 인덱스와 하한 인덱스가 같으면, 해당 수가 존재하지 않는 것이다.
    if upper_idx==lower_idx:
        print(-1)
    else:
        print(lower_idx)