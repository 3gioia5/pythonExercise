# 백준1978

n = int(input())
numbers = list(map(int, input().split()))
count = 0

for num in numbers:
    error = 0
    if num > 1:
        for i in range(2, num):
            if num % i == 0:
                error += 1
        if error == 0:
            count += 1

print(count)