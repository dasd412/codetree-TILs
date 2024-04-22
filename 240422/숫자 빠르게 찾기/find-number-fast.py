n,m = list(map(int, input().split()))
arr = list(map(int, input().split()))

def binary_search(number:int)->int:
    start=0
    end=len(arr)-1

    while start<=end:
        mid=(start+end)//2
        if arr[mid]==number:
            return mid+1
        elif arr[mid]<number:
            start=mid+1
        else:
            end=mid-1
    
    return -1


for i in range(m):
    number=int(input())
    print(binary_search(number))