# 백준1110

N = int(input())
number = N
count = 0

while True:
    a = number // 10
    b = number % 10
    c = (a + b) % 10

    number = b * 10 + c
    count += 1

    if number == N:
        break

print(count)