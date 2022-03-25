# 백준10156

k, n, m = map(int, input().split())

if m < k * n:
    print(abs(m - k * n))
else:
    print(0)
