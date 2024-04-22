import sys
m=int(input())
a,b= list(map(int, input().split()))

# b-a가 10^5이므로 10^8보다 작다. 
# b-a에 해당 하는 원소들에 대해 이진 탐색을 할 경우 각 원소마다 O(log n)이 걸린다.
# 따라서 b-a의 원소들에 대해 이진 탐색을 하면 O(n log n)정도 소요된다.

def binary_search(number:int):
    left=1
    right=m+1
    count=0

    while left<=right:
        mid=(left+right)//2
        count+=1
        if mid==number:
            return count
        elif mid<number:
            left=mid+1
        else:
            right=mid-1

mi=sys.maxsize
mx=-sys.maxsize

for i in range(a,b+1):
    count=binary_search(i)
    mi=min(mi,count)
    mx=max(mx,count)

print(str(mi)+' '+str(mx))