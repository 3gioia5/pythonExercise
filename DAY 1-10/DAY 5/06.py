# 백준1546

N = int(input())
scores = list(map(int, input().split()))

new_scores = []

M = max(scores)

for i in scores:
    new_scores.append(i / M * 100)

new_avg = sum(new_scores) / N

print(new_avg)

