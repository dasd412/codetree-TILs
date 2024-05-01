import math

n=int(input())

"""
1,2,m,4,m,m,7,8,m,m,11,m,13,14,m,16,17,m,19,m,m,22
,23,m,m,26,m,28,29,m,31....

11은 6번째 숫자. 11-3-2=6 (각각 3의 배수 개수, 5의 배수 개수)
16은 9번째 숫자. 16-5-3+1=9 (각각 3의 배수 개수, 5의 배수 개수, 15의 배수 개수)
31은 17번째 숫자. 31-10-6+2=17 (각각 3의 배수 개수, 5의 배수 개수, 15의 배수 개수)

번호 N이 커질수록 3의 배수 개수, 5의 배수 개수, 15의 배수 개수는 증가한다. 
이 배수 개수의 합을 x라 할 때, N과 x는 단조 증가 관계이다. 따라서 파라메트릭 서치를 활용한다.
"""

def get_sum(number:int)->int:
    sums=number

    sums-=(number//3)
    sums-=(number//5)
    sums+=(number//15)

    return sums

start=1
end=int(math.pow(10,30))

answer=0

while start<=end:
    mid=(start+end)//2

    x=get_sum(mid)

    if x<n:
        start=mid+1
    else:
        if x==n and mid%3!=0 and mid%5!=0:
            answer=mid
            break
        end=mid-1

print(answer)