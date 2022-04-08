# 백준9076

t = int(input())

for i in range(t):
    scores = list(map(int, input().split()))

    scores.remove(max(scores))
    scores.remove(min(scores))

    if max(scores) - min(scores) >= 4:
        print("KIN")
    else:
        print(sum(scores))
