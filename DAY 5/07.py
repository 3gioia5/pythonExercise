# 백준8958

N = int(input())

for i in range(N):
    line = input()
    sum_score = 0
    score = 0

    for k in line:
        if k == 'O':
            score += 1
            sum_score += score
        else:
            score = 0

    print(sum_score)