import sys

n=int(input())
k=int(input())

"""
수의 범위는 1이상 n*n이다.
번호 k가 올라갈수록 해당하는 수 x도 증가하는 단조 증가이다.

5*5 배열에서 6이 몇번째인지 찾아보자.
1번째 열에선 6보다 작거나 같은 값이 5개, 2번째열에선 3개, 3번째열에선 2개, 4번째열에선 1개, 5번째 열에선 1개로
6은 12번째 수임을 알 수 있다.

12는 1번째 열에서 12보다 작거나 같은 값이 5개, 2번째열에선 5개, 3번째 열에선 4개, 4번째열에선 3개, 5번째열에선 2개로
19번쨰 수다.
"""

left=1
right=25
right=sys.maxsize

def get_sequence(number:int):
    sequence=0
    for j in range(n):
        sequence+=min((number//(j+1)),n)
    return sequence

answer=sys.maxsize

while left<=right:
    mid=(left+right)//2

    # 수 mid가 몇 번째 수인지 알아낸다.
    sequence=get_sequence(mid)

    if sequence>=k:
        answer=min(answer,mid)
        right=mid-1
    else:
        left=mid+1

print(answer)