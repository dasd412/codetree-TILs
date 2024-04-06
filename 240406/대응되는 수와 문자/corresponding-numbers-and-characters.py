from collections import defaultdict

n,m = list(map(int, input().split()))

# num_dict[문자]=인덱스
num_dict=defaultdict(int)

# str_dict[인덱스]=문자
str_dict=defaultdict(int)

for i in range(n):
    s=input()
    num_dict[s]=i+1
    str_dict[i+1]=s

for i in range(m):
    s=input()
    if s.isdigit():
        print(str_dict[int(s)])
    else:
        print(num_dict[s])