n,m=list(map(int, input().split()))
arr=list(map(int, input().split()))
query=list(map(int, input().split()))

def lower_bound(number:int)->int:
    start=0
    end=len(arr)-1

    index=n

    while start<=end:
        mid=(start+end)//2

        if arr[mid]>=number:
            index=min(index,mid)
            end=mid-1
        else:
            start=mid+1

    return index

def upper_bound(number:int)->int:
    start=0
    end=len(arr)-1

    index=n

    while start<=end:
        mid=(start+end)//2
        
        if arr[mid]>number:
            index=min(index,mid)
            end=mid-1
        else:
            start=mid+1
    
    return index

for x in query:
    l_idx=lower_bound(x)
    u_idx=upper_bound(x)
    if l_idx==u_idx:
        print(-1)
    else:
        print(l_idx+1)