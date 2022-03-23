# 백준1181

import time

a = time.time()

n = int(input())
words = list()

for i in range(n):
    words.append(input())

words = list(set(words))
words.sort()
words.sort(key = len)

for i in words:
    print(i)

b = time.time()

print(b - a)