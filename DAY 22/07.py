# 백준10984

for i in range(int(input())):
    n = int(input())

    score = 0
    gpa = 0

    for j in range(n):
        c, g = map(float, input().split())

        score += c
        gpa += c * g

    print(int(score), round(gpa / score, 1))
