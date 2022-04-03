# 백준3058

t = int(input())

for _ in range(t):
    numbers = list(map(int, input().split()))
    even = list()

    for i in numbers:
        if i % 2 == 0:
            even.append(i)

    even.sort()

    print(sum(even), even[0])
