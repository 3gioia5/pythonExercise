# 백준1267

n = int(input())
t = list(map(int, input().split()))

y = 0
m = 0

for i in t:
    y += i // 30 * 10 + 10
    m += i // 60 * 15 + 15

if y > m:
    print("M", m)
elif y < m:
    print("Y", y)
else:
    print("Y M", y)
