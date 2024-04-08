n,k = list(map(int, input().split()))

nums=[i for i in range(n)]
arr=[set() for i in range(n)]

for i in range(n):
    arr[i].add(i)

order=[]
for i in range(k):
    a,b=list(map(int, input().split()))
    order.append((a-1,b-1))

# O(3*10^5)
order=order+order+order

# O(3*10^5)
for i in range(len(order)):
    a,b=order[i]

    arr[nums[a]].add(b)
    arr[nums[b]].add(a)

    temp=nums[a]
    nums[a]=nums[b]
    nums[b]=temp

# O(10^5)
for i in range(len(arr)):
    print(len(arr[i]))