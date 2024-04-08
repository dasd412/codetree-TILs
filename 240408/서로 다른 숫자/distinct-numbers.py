n = int(input())
arr = list(map(int, input().split()))

sets=set()
for elem in arr:
    sets.add(elem)

print(len(sets))