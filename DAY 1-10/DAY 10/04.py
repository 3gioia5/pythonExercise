# 백준1977

m = int(input())
n = int(input())
square = list()

for i in range(m, n + 1):
    if int(i ** 0.5) ** 2 == i:
        square.append(i)

if len(square) == 0:
    print(-1)
else:
    print(sum(square))
    print(min(square))
