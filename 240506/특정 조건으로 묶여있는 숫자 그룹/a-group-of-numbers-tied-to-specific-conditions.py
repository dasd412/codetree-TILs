n,k = list(map(int, input().split()))

arr=[]
for i in range(n):
    num=int(input())
    arr.append(num)

arr.sort()

length=0
s=-1
e=-1

# 가장 긴 그룹을 먼저 찾자. O(N)
for left in range(n-1):
    right=left
    while right<n:
        if abs(arr[left]-arr[right])<=k:
            if length<right-left+1:
                length=right-left+1
                s=left
                e=right
            right+=1
        else:
            break

#O(n)
arr=[arr[i] for i in range(n) if i<s or i>e]

second_length=0

# 두 번째 그룹을 찾자. O(N)
for left in range(len(arr)):
    right=left
    while right<len(arr):
        if abs(arr[left]-arr[right])<=k:
            if second_length<right-left+1:
                second_length=right-left+1
            right+=1
        else:
            break

# O(3N)
print(length+second_length)