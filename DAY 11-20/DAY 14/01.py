# 백준1629
# 시간 초과

a, b, c = map(int, input().split())

for i in range(b):
    a *= a

print(a % c)
