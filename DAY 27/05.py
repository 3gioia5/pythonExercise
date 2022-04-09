# 백준10409

n, t = map(int, input().split())
tasks = list(map(int, input().split()))

for i in range(n):
    if sum(tasks[:i + 1]) > t:
        print(i)
        break
    elif i == n - 1:
        print(n)
