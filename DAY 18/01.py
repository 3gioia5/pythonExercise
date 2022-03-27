# 백준10870

n = int(input())
current = 0
next = 1

for i in range(n):
    current, next = next, current + next

print(current)
