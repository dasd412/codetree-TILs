from collections import defaultdict

n = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
C = list(map(int, input().split()))
D = list(map(int, input().split()))

# ab[A+B]=개수 , cd [C+D]=개수
ab=defaultdict(int)
cd=defaultdict(int)

# O(n^2)
for i in range(n):
    for j in range(n):
        ab[A[i]+B[j]]+=1

# O(n^2)
for i in range(n):
    for j in range(n):
        cd[C[i]+D[j]]+=1

# len(ab)=O(n^2)
answer=0
for k1,v1 in ab.items():
    # 합이 0이 되는 경우 가짓수를 곱한다.
    if -k1 in cd:
        answer+=(v1*cd[-k1])

"""
원래라면 O(n^4)인데, 이러면 10^12이 되므로 시간 초과다.
해시맵을 활용하면 O(2n^2)으로 10^6이 되므로 충분히 풀 수 있다.
"""
print(answer)