n,m = list(map(int, input().split()))
a = list(map(int, input().split()))
b = list(map(int, input().split()))

def is_subsequence()->bool:

    # i는 a인덱스, j는 b인덱스
    i=0
    for j in range(m):
        
        while i<n and a[i]!=b[j]:
            i+=1
        # b의 원소를 기준으로 a에서 못찾았다면 부분 수열이 아님.
        if i==n:
            return False
        else:
            i+=1
        
    return True

if is_subsequence():
    print('Yes')
else:
    print('No')