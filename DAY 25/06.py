# 백준2455

max = ans = 0

for _ in range(4):
    o, i = map(int, input().split())
    ans -= o
    if max < ans:
        max = ans

    ans += i
    if max < ans:
        max = ans

print(max)
