# 백준2720

for i in range(int(input())):
    c = int(input())

    q = c // 25
    d = (c % 25) // 10
    n = ((c % 25) % 10) // 5
    p = (c % 5) // 1

    print(q, d, n, p)
