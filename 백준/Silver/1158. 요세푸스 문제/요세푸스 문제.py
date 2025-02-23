from collections import deque

n, k = map(int, input().split())
arr = deque(range(1, n + 1))
arr2 = []

while arr:
    arr.rotate(-(k-1))  # k-1 만큼 왼쪽으로 회전
    arr2.append(arr.popleft())  # 맨 앞의 원소를 제거하고 arr2에 추가

print("<" + ', '.join(map(str, arr2)) + ">")