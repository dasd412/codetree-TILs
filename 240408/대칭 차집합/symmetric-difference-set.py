n,m=list(map(int, input().split()))
a=set(map(int, input().split()))
b=set(map(int, input().split()))

o_a=a-b
o_b=b-a

oo_ab=o_a|o_b

print(len(oo_ab))