# 백준10250

t = int(input())

for i in range(t):
    h, w, n = map(int, input().split())

    floor = n % h
    number = n // h + 1

    if n % h == 0:
        number = n // h
        floor = h

    print(floor * 100 + number)
