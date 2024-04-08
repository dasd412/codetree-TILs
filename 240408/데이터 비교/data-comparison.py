n=int(input())
arr1 = list(map(int, input().split()))

m=int(input())
arr2 = list(map(int, input().split()))

arr1_set=set()
for elem in arr1:
    arr1_set.add(elem)

for elem in arr2:
    if elem in arr1:
        print(1,end=' ')
    else:
        print(0,end=' ')