import heapq

# O(nm)=10^10이므로 쌍을 만들기만 해도 시간초과다.
n,m,k=list(map(int,input().split()))

a=list(map(int,input().split()))
b=list(map(int,input().split()))

# O(nlogn + mlogm)
a.sort()
b.sort()

# O(nlogn)
# (원소의 합, a원소, b원소, 인덱스)
heap=[]
for elem in a:
    heapq.heappush(heap,(elem+b[0],elem,b[0],0))

# O(klogn)
# 정렬해서 b의 인덱스를 바로 찾아내는게 핵심이었다.
for i in range(k):
    ab,elem_a,elem_b,b_index=heapq.heappop(heap)

    if b_index+1<len(b):
        heapq.heappush(heap,(elem_a+b[b_index+1],elem_a,b[b_index+1],b_index+1))
    
    if i==k-1:  
        print(elem_a+elem_b)