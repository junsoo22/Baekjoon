from collections import deque

def can_convert(a, b):
    diff = 0

    for i in range(len(a)):
        if a[i] != b[i]:
            diff += 1

    return diff == 1


def solution(begin, target, words):

    if target not in words:
        return 0

    queue = deque([(begin, 0)])
    visited = set()

    while queue:
        word, cnt = queue.popleft()

        if word == target:
            return cnt

        for w in words:
            if w not in visited and can_convert(word, w):
                visited.add(w)
                queue.append((w, cnt + 1))

    return 0