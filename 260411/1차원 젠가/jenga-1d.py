n = int(input())
blocks = [int(input()) for _ in range(n)]
s1, e1 = map(int, input().split())
s2, e2 = map(int, input().split())

# Please write your code here.
# print(blocks)
blocks1=blocks[:s1-1]
blocks2=blocks[e1:]
# print(blocks1)
# print(blocks2)
sum_block=blocks1+blocks2
# print(sum_block)
blocks3=sum_block[:s2-1]
blocks4=sum_block[e2:]
# print(blocks4)
# print(blocks3)
answer=blocks3+blocks4
print(len(answer))
for i in answer:
    print(i)