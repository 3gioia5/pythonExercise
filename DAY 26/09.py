# 백준5800

k = int(input())

for i in range(k):
    scores = list(map(int, input().split()))

    n = scores[0]
    scores = scores[1:]
    scores.sort()

    gap = list()

    for j in range(len(scores) - 1):
        gap.append(scores[j + 1] - scores[j])

    print("Class", i + 1)
    print("Max {}, Min {}, Largest gap {}".
          format(max(scores), min(scores), max(gap)))
