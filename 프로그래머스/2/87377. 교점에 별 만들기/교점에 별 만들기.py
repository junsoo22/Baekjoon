from itertools import permutations, combinations
def solution(line):
    # print(line)
    points=set()
    for first, second in combinations(line, 2):
        a, b, e = first
        c, d, f = second

        denominator = a * d - b * c

        # 평행하거나 일치하는 직선
        if denominator == 0:
            continue

        x_numerator = b * f - e * d
        y_numerator = e * c - a * f

        # x와 y가 모두 정수인지 확인
        if x_numerator % denominator != 0:
            continue

        if y_numerator % denominator != 0:
            continue

        x = x_numerator // denominator
        y = y_numerator // denominator

        points.add((x, y))
    # print(points)
    
    # 별이 존재하는 좌표 범위
    min_x = min(x for x, y in points)
    max_x = max(x for x, y in points)
    min_y = min(y for x, y in points)
    max_y = max(y for x, y in points)
    # print(min_x, max_x,min_y,max_y)
    width = max_x - min_x + 1
    height = max_y-min_y + 1
    # print("width,height",width,height)
    answer = [["."] * width for _ in range(height)]
    for x, y in points:
        row = max_y - y
        column = x - min_x
        answer[row][column]='*'
    # print(answer)
    answer = ["".join(row) for row in answer]
    return answer