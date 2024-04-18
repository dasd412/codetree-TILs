n,k = list(map(int, input().split()))

numbers=[i+1 for i in range(n)]

postions=[{i} for i in range(n)]

arr=[]
for i in range(k):
    a,b=list(map(int, input().split()))
    arr.append((a,b))

arr=arr+arr+arr

# O(3K)
for i in range(len(arr)): 
    a,b=arr[i][0]-1,arr[i][1]-1

    postions[numbers[a]-1].add(b)
    postions[numbers[b]-1].add(a)

    temp=numbers[a]
    numbers[a]=numbers[b]
    numbers[b]=temp

# O(N)
for i in range(n):
    print(len(postions[i]))

# O(3K+N)