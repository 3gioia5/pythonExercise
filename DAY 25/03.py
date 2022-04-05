# 백준2750

n = int(input())
numbers = list()

for _ in range(n):
    ns = int(input())
    numbers.append(ns)

numbers.sort()

for i in numbers:
    print(i)
