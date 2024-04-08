n = int(input())
a = list(map(int, input().split()))

m = int(input())
b = list(map(int, input().split()))

a_set=set()

for elem in a:
    a_set.add(elem)

for elem in b:
    if elem in a_set:
        print(1)
    else:
        print(0)