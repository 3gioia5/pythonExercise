# 백준10103

n = int(input())
s = 100
c = 100

for i in range(n):
    score_s, score_c = map(int, input().split())

    if score_s > score_c:
        c -= score_s
    elif score_s < score_c:
        s -= score_c
    else:
        continue

print(s)
print(c)
