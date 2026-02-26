n=int(input())

words=[]
result=[]
for i in range(n):
    word=input()
    words.append(word)

words.sort()

count =0
for i in range(n):
    if i+1<n and words[i+1].startswith(words[i]):
        continue
    count+=1
print(count)