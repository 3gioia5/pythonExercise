# 백준1712

a, b, c = list(map(int, input().split()))

if b >= c:
    print(-1)
else:
    print(a // (c - b) + 1)