n,m=list(map(int, input().split()))
dots=list(map(int, input().split()))

dots.sort()

def lower_bound(number:int)->int:
    start=0
    end=n-1

    index=n

    while start<=end:
        mid=(start+end)//2

        if dots[mid]>=number:
            index=min(index,mid)
            end=mid-1
        else:
            start=mid+1

    return index

def custom_bound(number:int)->int:
    start=0
    end=n-1
    index=-1

    while start<=end:

        mid=(start+end)//2

        if dots[mid]<=number:
            index=max(index,mid)
            start=mid+1
        else:
            end=mid-1

    return index

# 주어지는 점 수가 10^10이므로 누적합 풀이는 불가능하다. -> 메모리 초과때문
for i in range(m):
    start,end=list(map(int, input().split()))
    # start보다 크거나 같은 숫자의 인덱스
    l_index=lower_bound(start)
    # end보다 작거나 같은 숫자의 인덱스
    r_index=custom_bound(end)
    if l_index<=r_index:
        print(r_index-l_index+1)
    else:
        print(0)