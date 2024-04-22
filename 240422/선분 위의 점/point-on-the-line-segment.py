n,m = list(map(int, input().split()))
arr = list(map(int, input().split()))
arr.sort()

def lower_bound(x:int)->int:
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
    
    return min_idx

def upper_bound(x:int)->int:
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
    
    return min_idx


for i in range(m):
    start,end=list(map(int, input().split()))

    left=lower_bound(start)
    right=upper_bound(end)

    print(right-left)