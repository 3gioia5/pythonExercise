# 백준1181
# 시간 단축할 수 있는 방법 찾아서 기록용

import sys
import time

a = time.time()

n = int(sys.stdin.readline())
word = list()

for i in range(n):
    word.append(sys.stdin.readline().strip())

word = list(set(word))
word.sort()
word.sort(key = len)

for i in word:
    print(i)

b = time.time()

print(b - a)
