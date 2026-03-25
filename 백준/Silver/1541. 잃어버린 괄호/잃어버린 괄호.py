n = input()

parts = n.split('-')

# 첫 번째는 더하기만
result = sum(map(int, parts[0].split('+')))

# 나머지는 전부 빼기
for i in parts[1:]:
    result -= sum(map(int, i.split('+')))

print(result)