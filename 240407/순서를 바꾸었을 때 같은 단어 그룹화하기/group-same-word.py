from collections import defaultdict

n = int(input())

counter=defaultdict(int)

# O(nm)
for i in range(n):
    word=input()
    # 정렬을 해서 알파벳순으로 하게 만듬.
    l_word=list(word)
    l_word.sort()

    word_cnt=defaultdict(int)
    
    for j in range(len(l_word)):
        word_cnt[l_word[j]]+=1
    
    counter[tuple(word_cnt.items())]+=1

answer=0
for k,v in counter.items():
    answer=max(answer,v)
print(answer)