n,m = list(map(int, input().split()))
arr = list(map(int, input().split()))

def lower_bound(number:int)->int:
    left=0
    right=n-1
    min_idx=n

    while left<=right:
        mid=(left+right)//2

        if arr[mid]>=number:
            min_idx=min(min_idx,mid)
            right=mid-1
        else:
            left=mid+1
    
    return min_idx


def upper_bound(number:int)->int:
    left=0
    right=n-1
    min_idx=n

    while left<=right:
        mid=(left+right)//2

        if arr[mid]>number:
            min_idx=min(min_idx,mid)
            right=mid-1
        else:
            left=mid+1
    
    return min_idx

for i in range(m):
    number=int(input())
    print(upper_bound(number)-lower_bound(number))