# 백준9325
# 2308ms...

t = int(input())

for i in range(t):
    s = int(input())
    n = int(input())

    options = 0

    for j in range(n):
        q, p = map(int, input().split())

        options += q * p

    print(s + options)
