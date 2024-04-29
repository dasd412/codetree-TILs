import sys

m=int(input())
a,b= list(map(int, input().split()))

def binary_search_count(number:int)->int:
    start=1
    end=m
    count=0

    while start<=end:
        mid=(start+end)//2
        count+=1

        if mid<number:
            start=mid+1
        elif mid==number:
            return count
        else:
            end=mid-1

    return count

max_time=-sys.maxsize
min_time=sys.maxsize

# O(10^5)*O(log 10^5)
for i in range(a,b+1):
    count=binary_search_count(i)
    max_time=max(max_time,count)
    min_time=min(min_time,count)

print(str(min_time)+' '+str(max_time))